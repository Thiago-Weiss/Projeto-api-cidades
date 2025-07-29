from fastapi import APIRouter
from fastapi.responses import JSONResponse
import pandas as pd

from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_UF

router = APIRouter()

@router.get("/estados")
def obter_estados():
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_UF])
    estados = df[NOME_UF].unique().tolist()
    return JSONResponse(content= estados)
