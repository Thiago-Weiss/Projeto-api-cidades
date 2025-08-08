from fastapi import APIRouter, Path, Query
import pandas as pd

from app.services import converter_para_o_front
from app.core import CIDADE_ESTADOS_ARQUIVO, CODE_CIDADE, NOME_ESTADO, NOME_CIDADE, CODE_CIDADE_COMPLETO, LATITUDE, LONGITUDE, RespostaFormato

router = APIRouter()



@router.get("/localizar-coordenada-por-codigo/{codigo}", summary= "Tenta traduzir o codigo passado para cidades, estado, regions...")
def localizar_coordenada_por_codigo(
    codigo: str = Path(..., pattern=r"^\d{5}$|^\d{7}$", description="Aceita código de cidade com 5 caracteres numericos ou codigo de cidade completa com 7 caracteres numericos"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):

    # adiciona a coluna de code no data frame
    colunas = [CODE_CIDADE, CODE_CIDADE_COMPLETO, NOME_ESTADO, NOME_CIDADE, LATITUDE, LONGITUDE]
    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= colunas)

    try:
        codigo_numero = int(codigo)
    except:
        return f"O codigo: {codigo} tem que ser um numero inteiro"


    # municipio
    if len(codigo) == 5:
        df = df[df[CODE_CIDADE] == codigo]
        df = df.drop_duplicates(subset=[CODE_CIDADE])
        return converter_para_o_front(df, resposta_formato)
    
    # municipio completo
    elif len(codigo) == 7:
        df = df[df[CODE_CIDADE_COMPLETO] == codigo_numero]
        df = df.drop_duplicates(subset=[CODE_CIDADE_COMPLETO])
        return converter_para_o_front(df, resposta_formato)

    else:
        return f"O codigo: {codigo} tem que ser um numero inteiro com 5 ou 7 caracteres numericos"
    
    
