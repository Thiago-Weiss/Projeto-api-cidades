from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd

from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO

router = APIRouter()

@router.get("/estados")
def obter_estados():
    
    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO])

    # pega todos os estados
    estados = df[NOME_ESTADO].unique().tolist()

    # retorna
    return JSONResponse(content= estados)
