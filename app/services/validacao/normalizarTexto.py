import unicodedata



# normaliza o texto removendo todos os acentos
def normalizar_texto(text: str) -> str:
    nfkd = unicodedata.normalize('NFD', text)
    return "".join(c for c in nfkd if unicodedata.category(c) != "Mn").lower().strip()