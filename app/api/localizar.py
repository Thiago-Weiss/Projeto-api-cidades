from fastapi import APIRouter, Path, Query
import pandas as pd
from app.core import RespostaFormato
from app.services import traduzir_codigo, converter_para_o_front



router = APIRouter()



@router.get("/localizar-codigo/{codigo}",
            summary= "Tenta traduzir o codigo passado", 
            description= "Tenta traduzir o codigo passado, retornando o dados como estado, cidade, distrito")
def localizar_codigo(
    codigo: str = Path(..., pattern=r"^\d{2,9}$", description="Código entre 2 e 9 caracteres numericos"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):
    df = traduzir_codigo(codigo)

    # se retornar um erro
    if isinstance(df, str):
        return df

    # se nao achar nenhum dado
    if df.empty:
        return f"Nenhum dado achado para o codigo: {codigo}, Provavel que estejá errado"

    return converter_para_o_front(df, resposta_formato)


