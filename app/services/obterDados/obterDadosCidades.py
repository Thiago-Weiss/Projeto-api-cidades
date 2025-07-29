from os import makedirs, path
import requests
import zipfile
import pandas as pd
import shutil

# meus arquivos
from app.core import CIDADE_ESTADOS_ARQUIVO_ORIGINAL, CIDADE_ESTADOS_ARQUIVO, COLUNAS_PADRAO, TIPOS_COLUNAS



def processar_arquivo_cidades_base():
    # se nao tem o arquivo base
    if not path.exists(CIDADE_ESTADOS_ARQUIVO_ORIGINAL):
        return


    # abre o arquivo
    df = pd.read_excel(
        CIDADE_ESTADOS_ARQUIVO_ORIGINAL,
        engine='odf',
        dtype=str,
        skiprows=6,
        usecols=range(12))
    
    # renomeia as colunas
    df.columns = COLUNAS_PADRAO

    # define o tipo de dado pra cada coluna
    for coluna, tipo in TIPOS_COLUNAS.items():
        df[coluna] = df[coluna].astype(tipo)

    # remove as linhas com valores ausentes 
    # NAO TEM nenhuma com dado ausente
    print(df.isna().sum())  
    df = df.dropna()

    df.to_parquet(CIDADE_ESTADOS_ARQUIVO)





