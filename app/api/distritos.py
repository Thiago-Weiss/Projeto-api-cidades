from fastapi import APIRouter, Query
import pandas as pd


from app.core import CIDADE_ESTADOS_ARQUIVO, NOME_ESTADO, NOME_CIDADE, NOME_CIDADE_NORMALIZADO, NOME_DISTRITO, CODE_DISTRITO_COMPLETO, RespostaFormato
from app.services import validar_estado, normalizar_texto, converter_para_o_front

router = APIRouter()


@router.get("/distritos",
            summary= "Lista os distritos de cidade", 
            description= "Retorna uma lista dos distritos da cidades e estado informado, opcionalmente pode retornar junto o codigo e definir o formato da resposta.")

def obter_cidades_por_estado(
    estado: str = Query(..., description= "Pode ser o **nome** ou a **sigla** do estado. Exemplos: `SC`, `Santa Catarina`, `santa catarina`, `SANTA catarina`"),
    cidade: str = Query(..., description= "O nome da cidade podendo ser, `Florianópolis`, `Florianopolis`, `florianopolis` "),
    codigos: bool = Query(default= False, description= "Quer os codigos dos estados tambem, exp: Rio de Janeiro : 33, SC : 42"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):

    # valida o estado
    estado_valido = validar_estado(estado)
    if not estado_valido:
        return {f"error": "Estado:{estado} não encontrado ou formato inválido tente passar um estado da api /estados"}

    # normaliza o nome da cidade
    cidade_normalizada = normalizar_texto(cidade)

    # adiciona a coluna de code no data frame
    colunas = [NOME_ESTADO, NOME_CIDADE, NOME_CIDADE_NORMALIZADO, NOME_DISTRITO]
    if codigos:
        colunas.append(CODE_DISTRITO_COMPLETO)

    # abre o arquivo
    df = pd.read_parquet(CIDADE_ESTADOS_ARQUIVO, columns= colunas)

    # cria o df dos distritos
    df = df[
        (df[NOME_ESTADO] == estado_valido) &
        (df[NOME_CIDADE_NORMALIZADO] == cidade_normalizada)
    ]

    # verifica se achou a cidade no estado
    if df.empty:
        return {"error": f"Cidade '{cidade}' não encontrada no estado {estado_valido}"}

    # nao vai fazer nada pq os distritos nao se repetem, pq nao mais dados como ruas ou quadras
    df = df.drop_duplicates(subset=[NOME_DISTRITO])

    return converter_para_o_front(df, resposta_formato)

