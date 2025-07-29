import unicodedata

ESTADOS_MAP = {
    "rondonia": "Rondônia",
    "ac": "Acre",
    "acre": "Acre",
    "amazonas": "Amazonas",
    "rr": "Roraima",
    "roraima": "Roraima",
    "pa": "Pará",
    "para": "Pará",
    "amapa": "Amapá",
    "ap": "Amapá",
    "tocantins": "Tocantins",
    "ma": "Maranhão",
    "maranhao": "Maranhão",
    "piaui": "Piauí",
    "pi": "Piauí",
    "ceara": "Ceará",
    "ce": "Ceará",
    "rio grande do norte": "Rio Grande do Norte",
    "rn": "Rio Grande do Norte",
    "paraiba": "Paraíba",
    "pb": "Paraíba",
    "pernambuco": "Pernambuco",
    "pe": "Pernambuco",
    "alagoas": "Alagoas",
    "al": "Alagoas",
    "sergipe": "Sergipe",
    "se": "Sergipe",
    "bahia": "Bahia",
    "ba": "Bahia",
    "minas gerais": "Minas Gerais",
    "mg": "Minas Gerais",
    "espirito santo": "Espírito Santo",
    "es": "Espírito Santo",
    "rio de janeiro": "Rio de Janeiro",
    "rj": "Rio de Janeiro",
    "sao paulo": "São Paulo",
    "sp": "São Paulo",
    "parana": "Paraná",
    "pr": "Paraná",
    "santa catarina": "Santa Catarina",
    "sc": "Santa Catarina",
    "rio grande do sul": "Rio Grande do Sul",
    "rs": "Rio Grande do Sul",
    "mato grosso do sul": "Mato Grosso do Sul",
    "ms": "Mato Grosso do Sul",
    "mato grosso": "Mato Grosso",
    "mt": "Mato Grosso",
    "goias": "Goiás",
    "go": "Goiás",
    "distrito federal": "Distrito Federal",
    "df": "Distrito Federal",
}

# normaliza o texto removendo todos os acentos
def normalize_text(text: str) -> str:
    nfkd = unicodedata.normalize('NFKD', text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)]).lower().strip()


def validar_estado(estado : str) -> str:
    estado_normalizado = normalize_text(estado)
    print(estado_normalizado)
    return ESTADOS_MAP.get(estado_normalizado)

