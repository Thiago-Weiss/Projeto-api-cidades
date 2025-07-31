import pandas as pd
from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, CODE_ESTADO, CODE_REGIAO_INTERMEDIARIA, NOME_REGIAO_INTERMEDIARIA, CODE_REGIAO_IMEDIATA, NOME_REGIAO_IMEDIATA, CODE_CIDADE, CODE_CIDADE_COMPLETO, NOME_CIDADE, CODE_BAIRRO, CODE_BAIRRO_COMPLETO, NOME_BAIRRO


def traduzir_codigo(codigo : str):
    tamanho_code = len(codigo)
    codigo_numero = 0
    try:
        codigo_numero = int(codigo)
    except:
        return f"O codigo: {codigo} tem que ser um numero inteiro"


    match tamanho_code:
        # estado
        case 2:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [CODE_ESTADO, NOME_ESTADO])
            df = df[df[CODE_ESTADO] == codigo_numero]
            return df.drop_duplicates()

        # regiao intermediaria 
        case 4:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[CODE_ESTADO, NOME_ESTADO, CODE_REGIAO_INTERMEDIARIA, NOME_REGIAO_INTERMEDIARIA])
            df = df[df[CODE_REGIAO_INTERMEDIARIA] == codigo_numero]
            return df.drop_duplicates()

        # regiao imediata
        case 6:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[CODE_ESTADO, NOME_ESTADO, CODE_REGIAO_INTERMEDIARIA, NOME_REGIAO_INTERMEDIARIA, CODE_REGIAO_IMEDIATA, NOME_REGIAO_IMEDIATA])
            df = df[df[CODE_REGIAO_IMEDIATA] == codigo_numero]
            return df.drop_duplicates()

        # municipio
        case 5:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[CODE_ESTADO, NOME_ESTADO, CODE_REGIAO_INTERMEDIARIA, NOME_REGIAO_INTERMEDIARIA, CODE_REGIAO_IMEDIATA, NOME_REGIAO_IMEDIATA, CODE_CIDADE, CODE_CIDADE_COMPLETO, NOME_CIDADE])
            df = df[df[CODE_CIDADE] == codigo]
            return df.drop_duplicates()
        
        # municipio completo
        case 7:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[CODE_ESTADO, NOME_ESTADO, CODE_REGIAO_INTERMEDIARIA, NOME_REGIAO_INTERMEDIARIA, CODE_REGIAO_IMEDIATA, NOME_REGIAO_IMEDIATA, CODE_CIDADE, CODE_CIDADE_COMPLETO, NOME_CIDADE])
            df = df[df[CODE_CIDADE_COMPLETO] == codigo_numero]
            return df.drop_duplicates()
        
        # bairro
        case 9:
            df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[CODE_ESTADO, NOME_ESTADO, CODE_REGIAO_INTERMEDIARIA, NOME_REGIAO_INTERMEDIARIA, CODE_REGIAO_IMEDIATA, NOME_REGIAO_IMEDIATA, CODE_CIDADE, CODE_CIDADE_COMPLETO, NOME_CIDADE, CODE_BAIRRO, CODE_BAIRRO_COMPLETO, NOME_BAIRRO])
            df = df[df[CODE_BAIRRO_COMPLETO] == codigo_numero]
            return df.drop_duplicates()
        
        case _:
            return f"Nenhum dado achado para o codigo: {codigo}, Provavel que estejá errado"