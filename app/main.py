from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from contextlib import asynccontextmanager
import sys


from app.core import CIDADE_ESTADOS_ARQUIVO
from app.api import bairros, estados, cidades, localizarCodigo, localizarCoordenadasPorEstadoCidade, localizarNome, localizarCoordenadaPorCodigo, localizarCoordenada

@asynccontextmanager
async def lifespan(app: FastAPI):
    # encerra o programa se nao achar o arquivo
    if not CIDADE_ESTADOS_ARQUIVO.exists():
        print(f"[ERRO] Arquivo {CIDADE_ESTADOS_ARQUIVO} não encontrado.")
        sys.exit(1)

    yield

    
app = FastAPI(lifespan=lifespan)


@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")

# Inclui os roteadores
app.include_router(estados.router)
app.include_router(cidades.router)
app.include_router(bairros.router)
app.include_router(localizarCodigo.router)
app.include_router(localizarNome.router)
app.include_router(localizarCoordenadasPorEstadoCidade.router)
app.include_router(localizarCoordenadaPorCodigo.router)
app.include_router(localizarCoordenada.router)



# rodar "python -m uvicorn app.main:app --reload"


