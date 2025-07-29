from fastapi import APIRouter, Query
import pandas as pd


from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_CIDADE, NOME_CIDADE_NORMALIZADO, NOME_DISTRITO
from app.services import validar_estado, normalizar_texto

router = APIRouter()


@router.get("/distritos")
def obter_cidades_por_estado(
    estado: str = Query(..., description= "Pode ser o **nome** ou a **sigla** do estado. Exemplos: `SC`, `Santa Catarina`, `santa catarina`, `SANTA catarina`"),
    cidade: str = Query(..., description= "O nome da cidade podendo ser, `Florianópolis`, `Florianopolis`, `florianopolis` ")
    ):

    # valida o estado
    estado_valido = validar_estado(estado)
    if not estado_valido:
        return {f"error": "Estado:{estado} não encontrado ou formato inválido tente passar um estado da api /estados"}

    # normaliza o nome da cidade
    cidade_normalizada = normalizar_texto(cidade)

    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[NOME_ESTADO, NOME_CIDADE, NOME_CIDADE_NORMALIZADO, NOME_DISTRITO])

    # cria o df dos estados
    df_estado = df[df[NOME_ESTADO] == estado_valido]

    # cria o df das cidades
    df_cidade = df_estado[df_estado[NOME_CIDADE_NORMALIZADO] == cidade_normalizada]

    # verifica se achou a cidade no estado
    if df_cidade.empty:
        return {"error": f"Cidade '{cidade}' não encontrada no estado {estado_valido}"}

    distritos = df_cidade[NOME_DISTRITO].drop_duplicates().tolist()

    # Filtra só as cidades do estado validado
    cidades_df = df[df[NOME_ESTADO] == estado_valido]

    # retorna
    return {
        "estado": estado_valido,
        "cidade": cidade,
        "distritos": distritos
    }