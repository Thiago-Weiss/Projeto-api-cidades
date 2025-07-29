from fastapi import APIRouter, Query
import pandas as pd


from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_MUNICIPIO
from app.services import validar_estado

router = APIRouter()


@router.get("/cidades")
def obter_cidades_por_estado(estado: str = Query(..., description="Nome ou sigla do estado")):

    estado_valido = validar_estado(estado)
    if not estado_valido:
        return {f"error": "Estado:{estado} não encontrado ou formato inválido tente passar um estado da api /estados"}

    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns=[NOME_ESTADO, NOME_MUNICIPIO])

    # Filtra só as cidades do estado validado
    cidades_df = df[df[NOME_ESTADO] == estado_valido]

    # Retorna lista com nomes das cidades (sem duplicatas, se for o caso)
    cidades = cidades_df[NOME_MUNICIPIO].drop_duplicates().tolist()

    return {"estado": estado_valido, "cidades": cidades}