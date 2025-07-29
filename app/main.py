from fastapi import FastAPI
from contextlib import asynccontextmanager
import sys


from app.core import CIDADE_ESTADOS_ARQUIVO
from app.api import estados, cidades

@asynccontextmanager
async def lifespan(app: FastAPI):
    # encerra o programa se nao achar o arquivo
    if not CIDADE_ESTADOS_ARQUIVO.exists():
        print(f"[ERRO] Arquivo {CIDADE_ESTADOS_ARQUIVO} não encontrado.")
        sys.exit(1)

    yield

    
app = FastAPI(lifespan=lifespan)



# Inclui os roteadores
app.include_router(estados.router)
app.include_router(cidades.router)




# rodar "python -m uvicorn app.main:app --reload"