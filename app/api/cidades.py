from fastapi import APIRouter, Query
import pandas as pd


from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_CIDADE
from app.services import validar_estado

router = APIRouter()


@router.get("/cidades")
def obter_cidades_por_estado(estado: str = Query(..., description="Retorna as cidades do estado passado. Pode ser o **nome** ou a **sigla** do estado. Exemplos: `SC`, `Santa Catarina`, `santa catarina`, `SANTA catarina`")):

    # valida o estado
    estado_valido = validar_estado(estado)
    if not estado_valido:
        return {f"error": "Estado:{estado} não encontrado ou formato inválido tente passar um estado da api /estados"}

    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[NOME_ESTADO, NOME_CIDADE])

    # Filtra só as cidades do estado validado
    df_estado = df[df[NOME_ESTADO] == estado_valido]

    # Retorna lista com nomes das cidades (sem duplicatas, se for o caso)
    cidades = df_estado[NOME_CIDADE].drop_duplicates().tolist()

    return {"estado": estado_valido, "cidades": cidades}