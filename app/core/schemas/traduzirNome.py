from enum import Enum


class RangePesquisa(str, Enum):
    ESTADOS = "ESTADOS"
    REGIAO_INTERMEDIARIA = "REGIAO_INTERMEDIARIA"
    REGIAO_IMEDIATA = "REGIAO_IMEDIATA"
    CIDADE = "CIDADE"
    BAIRRO = "BAIRRO"




class FormaPesquisa(str, Enum):
    EXATO = "EXATO"
    PALAVRA = "PALAVRA"
    CONTEM = "CONTEM"
