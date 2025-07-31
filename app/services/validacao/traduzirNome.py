import pandas as pd
from app.core import RangePesquisa, FormaPesquisa, CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA, NOME_REGIAO_IMEDIATA, NOME_CIDADE, NOME_CIDADE_NORMALIZADO, NOME_DISTRITO
from app.services import normalizar_texto

COLUNA_NORMALIZADA = "COLUNA_NORMALIZADA"

def filtrar_coluna(df : pd.DataFrame, coluna : str, nome_normalizado: str, forma_pesquisa: FormaPesquisa) -> pd.DataFrame:
    match forma_pesquisa:
        case FormaPesquisa.EXATO:
            df = df[df[coluna] == nome_normalizado]
            df = df.drop(columns=[coluna])
            df = df.drop_duplicates()
            return df

        case FormaPesquisa.PALAVRA:
            df = df[df[coluna].str.contains(rf"\b{nome_normalizado}\b", case=False, na=False, regex=True)]
            df = df.drop(columns=[coluna])
            df = df.drop_duplicates()
            return df

        case FormaPesquisa.CONTEM:
            df = df[df[coluna].str.contains(nome_normalizado, case=False, na=False)]
            df = df.drop(columns=[coluna])
            df = df.drop_duplicates()
            return df




def pesquisar_nome(nome : str, renge_pesquisa : RangePesquisa, forma_pesquisa : FormaPesquisa):
    nome_normalizado = normalizar_texto(nome)

    match renge_pesquisa:
        case renge_pesquisa.ESTADOS:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO])
            df[COLUNA_NORMALIZADA] = df[NOME_ESTADO].apply(normalizar_texto)
            df = filtrar_coluna(df, COLUNA_NORMALIZADA, nome_normalizado, forma_pesquisa)
            return df


        case renge_pesquisa.REGIAO_INTERMEDIARIA:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA])
            df[COLUNA_NORMALIZADA] = df[NOME_REGIAO_INTERMEDIARIA].apply(normalizar_texto)
            df = filtrar_coluna(df, COLUNA_NORMALIZADA, nome_normalizado, forma_pesquisa)
            return df

        case renge_pesquisa.REGIAO_IMEDIATA:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA, NOME_REGIAO_IMEDIATA])
            df[COLUNA_NORMALIZADA] = df[NOME_REGIAO_INTERMEDIARIA].apply(normalizar_texto)
            df = filtrar_coluna(df, COLUNA_NORMALIZADA, nome_normalizado, forma_pesquisa)
            return df

        case renge_pesquisa.CIDADE:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA, NOME_REGIAO_IMEDIATA, NOME_CIDADE, NOME_CIDADE_NORMALIZADO])
            df = filtrar_coluna(df, NOME_CIDADE_NORMALIZADO, nome_normalizado, forma_pesquisa)
            return df
        
        case renge_pesquisa.DISTRITO:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA, NOME_REGIAO_IMEDIATA, NOME_CIDADE, NOME_DISTRITO])
            df[COLUNA_NORMALIZADA] = df[NOME_DISTRITO].apply(normalizar_texto)
            df = filtrar_coluna(df, COLUNA_NORMALIZADA, nome_normalizado, forma_pesquisa)
            return df



