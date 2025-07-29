from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
import pandas as pd

from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, CODE_ESTADO, RespostaFormato
from app.services import converter_para_o_front



router = APIRouter()

@router.get("/estados",
            summary= "Lista os estados Brasileiros", 
            description= "Retorna uma lista dos estados Brasileiros, opcionalmente pode retornar junto o codigo e definir o formato da resposta.")
def obter_estados(
    codigos: bool = Query(default= False, description= "Quer os codigos dos estados tambem, exp: Rio de Janeiro : 33, SC : 42"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.LISTAS, description= "Formato da resposta")
    ):
    
    colunas = [NOME_ESTADO]
    if codigos:
        colunas.append(CODE_ESTADO)

    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= colunas)
    df = df.drop_duplicates(subset=[NOME_ESTADO])

    return converter_para_o_front(df, resposta_formato)


