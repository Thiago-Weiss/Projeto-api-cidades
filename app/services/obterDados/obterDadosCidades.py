from os import path
import pandas as pd
import geopandas as gpd


# meus arquivos
from app.core import CIDADE_ESTADOS_ARQUIVO_ORIGINAL, CIDADE_ESTADOS_ARQUIVO_ORIGINAL, CIDADE_ESTADOS_ARQUIVO, COLUNAS_PADRAO, TIPOS_COLUNAS, NOME_CIDADE, NOME_CIDADE_NORMALIZADO, CORDENADAS_ARQUIVO_ORIGINAL, CENTROIDE, LATITUDE, LONGITUDE, CD_MUN, CODE_CIDADE_COMPLETO
from app.services.validacao.normalizarTexto import normalizar_texto


def processar_arquivo_cidades_base():
    # se nao tem o arquivo base
    if not path.exists(CIDADE_ESTADOS_ARQUIVO_ORIGINAL):
        return


    # abre o arquivo
    df_cidades_estados = pd.read_excel(
        CIDADE_ESTADOS_ARQUIVO_ORIGINAL,
        engine='odf',
        dtype=str,
        skiprows=6,
        usecols=range(12))
    
    # renomeia as colunas
    df_cidades_estados.columns = COLUNAS_PADRAO

    # define o tipo de dado pra cada coluna
    for coluna, tipo in TIPOS_COLUNAS.items():
        df_cidades_estados[coluna] = df_cidades_estados[coluna].astype(tipo)

    # remove as linhas com valores ausentes 
    # NAO TEM nenhuma com dado ausente
    print(df_cidades_estados.isna().sum())  
    df_cidades_estados = df_cidades_estados.dropna()

    # cria uma coluna nova com o nome dos municipios normalizados
    df_cidades_estados[NOME_CIDADE_NORMALIZADO] = df_cidades_estados[NOME_CIDADE].apply(normalizar_texto)



    # agora cria o df_cidades_estados das cordenadas
    # Carrega o shapefile
    gdf = gpd.read_file(CORDENADAS_ARQUIVO_ORIGINAL, columns=[CENTROIDE, CD_MUN])

    # Reprojeta para um sistema métrico (UTM zone 23S - EPSG:31983)
    gdf_proj = gdf.to_crs(epsg=31983)

    # Calcula o centroide no sistema projetado e converte de volta para WGS84 (latitude/longitude)
    gdf[CENTROIDE] = gdf_proj.centroid.to_crs(epsg=4326)

    # Extrai latitude e longitude do centroide
    gdf[LATITUDE] = gdf[CENTROIDE].y
    gdf[LONGITUDE] = gdf[CENTROIDE].x


    # Seleciona colunas desejadas
    df_cordenada = gdf[[CD_MUN, LATITUDE, LONGITUDE]]

    # renomeia a coluna pra terem o mesmo nome nos dois dataframes
    df_cordenada = df_cordenada.rename(columns={CD_MUN: CODE_CIDADE_COMPLETO})

    # converte para int o codigo da cidade
    df_cordenada[CODE_CIDADE_COMPLETO] = df_cordenada[CODE_CIDADE_COMPLETO].astype(int)

    # junta os data frames
    df_cordenada = df_cordenada.merge(df_cidades_estados, on=CODE_CIDADE_COMPLETO, how= "left")

    # salva o arquivo
    df_cordenada.to_parquet(CIDADE_ESTADOS_ARQUIVO, index= False )




