from fastapi import APIRouter, Path, Query
from app.core import RespostaFormato, RangePesquisa, FormaPesquisa
from app.services import pesquisar_nome, converter_para_o_front



router = APIRouter()



@router.get("/localizar-nome/{nome}",
            summary= "Tenta traduzir o nome passado", 
            description= "Tenta traduzir o nome passado, retornando o dados como estado, cidade, distrito... que contenham o nome")

def localizar_nome(
    nome: str = Path(..., description="Passe um nome e uma forma de pesquisa pra tentar achar algo relacionando"),
    renge_pesquisa : RangePesquisa = Query(default= RangePesquisa.CIDADE, description= "Define o renge de cusca para o nome. exp: procura um estado, uma cidade, uma regiao"),
    forma_pesquisa : FormaPesquisa = Query(default= FormaPesquisa.PALAVRA, description=(
        "Define o modo de pesquisa pelo nome:\n"
        "- **EXATO** → retorna apenas registros com o nome exatamente igual ao termo pesquisado.\n"
        "- **PALAVRA** → retorna registros que contenham a palavra completa (ex.: 'joao' encontra 'joao pessoa', mas não 'joaoaaaa').\n"
        "- **CONTEM** → retorna registros que contenham o termo em qualquer parte do nome (ex.: 'joao' encontra 'joaoaaaa' ou 'aaajoao')."
    )),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):


    df = pesquisar_nome(nome, renge_pesquisa, forma_pesquisa)

    # se retornar um erro
    if isinstance(df, str):
        return df

    # se nao achar nenhum dado
    if df.empty:
        return f"Nenhum dado achado para o nome: {nome}, Provavel que estejá errado ou não exista, tente pesquisar por outra forma de pesquisa"

    return converter_para_o_front(df, resposta_formato)


