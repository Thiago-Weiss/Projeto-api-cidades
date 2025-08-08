from fastapi import APIRouter, Query
import pandas as pd

from app.services import validar_estado, normalizar_texto, converter_para_o_front
from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_CIDADE_NORMALIZADO, LATITUDE, LONGITUDE, RespostaFormato

router = APIRouter()



@router.get("/localizar-coordenada-por-estado-cidade", summary= "Converte o estado e cidade passadas para cordenadas geograficos")
def localizar_coordenada_estado_cidade(
    estado: str = Query(..., description= "Pode ser o **nome** ou a **sigla** do estado. Exemplos: `SC`, `Santa Catarina`, `santa catarina`, `SANTA catarina`"),
    cidade: str = Query(..., description= "O nome da cidade podendo ser, `Florianópolis`, `Florianopolis`, `florianopolis` "),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):
    # valida o estado
    estado_valido = validar_estado(estado)
    if not estado_valido:
        return {f"error": "Estado:{estado} não encontrado ou formato inválido tente passar um estado da api /estados"}

    # normaliza o nome da cidade
    cidade_normalizada = normalizar_texto(cidade)

    # adiciona a coluna de code no data frame
    colunas = [NOME_ESTADO, NOME_CIDADE_NORMALIZADO, LATITUDE, LONGITUDE]
    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= colunas)

    # filtra por estado e cidade
    df = df[(df[NOME_ESTADO] == estado_valido) & (df[NOME_CIDADE_NORMALIZADO] == cidade_normalizada)]

    # se nao estiver vazio
    if df.empty:
        return {"error": f"Cidade '{cidade}' não encontrada no estado {estado_valido}"}

    # remove os duplicados
    df = df.drop_duplicates(subset=[NOME_CIDADE_NORMALIZADO])

    # retorna
    return converter_para_o_front(df, resposta_formato)
