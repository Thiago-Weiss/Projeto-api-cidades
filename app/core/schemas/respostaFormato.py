from enum import Enum


class RespostaFormato(str, Enum):
    LISTAS_DE_LISTAS = "lista_de_listas"
    OBJETO = "objeto"
    LISTAS = "listas"
