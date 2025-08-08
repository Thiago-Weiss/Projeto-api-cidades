from math import radians, sin, cos, sqrt, atan2, degrees
from fastapi import APIRouter, Query
import pandas as pd

from app.services import converter_para_o_front
from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA, NOME_REGIAO_IMEDIATA, NOME_CIDADE, LATITUDE, LONGITUDE, RespostaFormato

router = APIRouter()




def calcular_distancia_direcao(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km

    # Distância Haversine
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    distancia = R * 2 * atan2(sqrt(a), sqrt(1 - a))

    # Cálculo do ângulo/direção em graus (bearing)
    y = sin(dlon) * cos(radians(lat2))
    x = cos(radians(lat1)) * sin(radians(lat2)) - sin(radians(lat1)) * cos(radians(lat2)) * cos(dlon)
    direcao_rad = atan2(y, x)
    direcao_graus = (degrees(direcao_rad) + 360) % 360  # Normaliza para 0–360°

    return round(distancia, 2), round(direcao_graus, 2)



@router.get("/localizar-coordenada", summary= "Tenta traduzir coordenada passada para cidades, estado, regions...")
def localizar_coordenada(
    latitude: float = Query(...),
    longitude: float = Query(...),
    distancia_max: int = Query(default=50, description= "Distancia maxima de procura de cidades proximas a coordenada pasada"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):

    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= [NOME_ESTADO, NOME_REGIAO_INTERMEDIARIA, NOME_REGIAO_IMEDIATA, NOME_CIDADE, LATITUDE, LONGITUDE])

    df[["DISTANCIA", "DIRECAO"]] = df.apply(
        lambda row: pd.Series(calcular_distancia_direcao(latitude, longitude, row[LATITUDE], row[LONGITUDE])),
        axis=1
    )


    df = df[df["DISTANCIA"] <= distancia_max]

    df = df.drop_duplicates(subset=[NOME_CIDADE])


    return converter_para_o_front(df, resposta_formato)
