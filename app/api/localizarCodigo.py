from fastapi import APIRouter, Path, Query
from app.core import RespostaFormato
from app.services import traduzir_codigo, converter_para_o_front



router = APIRouter()



@router.get("/localizar-codigo/{codigo}",
            summary= "Tenta traduzir o codigo passado", 
            description=(
                "Tenta traduzir o código passado, retornando dados como estado, cidade ou distrito.\n\n"
                "**Tamanhos de código aceitos:**\n"
                "- **2 dígitos** → Estado (UF)\n"
                "- **4 dígitos** → Região intermediária\n"
                "- **5 dígitos** → Região imediata\n"
                "- **5 dígitos** → Município\n"
                "- **7 dígitos** → Município completo\n"
                "- **9 dígitos** → Distrito completo"
            ))
def localizar_codigo(
    codigo: str = Path(..., pattern=r"^\d{2,9}$", description="Código entre 2 e 9 caracteres numericos"),
    resposta_formato: RespostaFormato = Query(default= RespostaFormato.OBJETO, description= "Formato da resposta")
    ):
    df = traduzir_codigo(codigo)

    # se retornar um erro
    if isinstance(df, str):
        return df

    # se nao achar nenhum dado
    if df.empty:
        return f"Nenhum dado achado para o codigo: {codigo}, Provavel que estejá errado"

    return converter_para_o_front(df, resposta_formato)


