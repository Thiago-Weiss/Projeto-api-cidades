from enum import Enum


class RangePesquisa(str, Enum):
    TUDO = "TUDO"
    ESTADOS = "ESTADOS"
    REGIAO_INTERMEDIARIA = "REGIAO_INTERMEDIARIA"
    REGIAO_IMEDIATA = "REGIAO_IMEDIATA"
    CIDADE = "CIDADE"
    DISTRITO = "DISTRITO"




class FormaPesquisa(str, Enum):
    EXATO = "EXATO"
    PALAVRA = "PALAVRA"
    CONTEM = "CONTEM"
