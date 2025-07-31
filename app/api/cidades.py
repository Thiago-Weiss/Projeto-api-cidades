from fastapi import APIRouter, Query
import pandas as pd


from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_CIDADE, CODE_CIDADE_COMPLETO, RespostaFormato
from app.services import validar_estado, converter_para_o_front

router = APIRouter()


@router.get("/cidades",
            summary= "Lista as cidades de um estado", 
            description= "Retorna uma lista das cidades do estado informado, opcionalmente pode retornar junto o codigo e definir o formato da resposta.")
def obter_cidades(
    estado: str = Query(..., description="Retorna as cidades do estado passado. Pode ser o **nome** ou a **sigla** do estado. Exemplos: `SC`, `Santa Catarina`, `santa catarina`, `SANTA catarina`"),
    codigos: bool = Query(default= False, description= "Quer os codigos dos estados tambem, exp: Rio de Janeiro : 33, SC : 42"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):

    # valida o estado
    estado_valido = validar_estado(estado)
    if not estado_valido:
        return {f"error": "Estado:{estado} não encontrado ou formato inválido tente passar um estado da api /estados"}
    

    # adiciona a coluna de code no data frame
    colunas = [NOME_ESTADO, NOME_CIDADE]
    if codigos:
        colunas.append(CODE_CIDADE_COMPLETO)

    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= colunas)

    # Filtra só as cidades do estado validado
    df = df[df[NOME_ESTADO] == estado_valido]

    df = df.drop_duplicates(subset=[NOME_CIDADE])

    return converter_para_o_front(df, resposta_formato, True)