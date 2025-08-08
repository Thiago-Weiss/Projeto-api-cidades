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

    
app = FastAPI(
    lifespan=lifespan,
    title="Brasil GeoAPI",
    description="""
Esta API fornece informações sobre estados, cidades, regiões e bairros.

## Funcionalidades principais

- ✅ Listar todos os estados do Brasil  
- ✅ Listar cidades de um estado  
- ✅ Listar bairros de uma cidade  
- ✅ Traduzir códigos IBGE para localizações  
  Ex: `42` → **Santa Catarina**
- ✅ Buscar por nomes para ver possíveis locais correspondentes  
  Ex: pesquisando **"Santa Maria"** na opção de cidades retorna duas:  
    - Santa Maria (Rio Grande do Norte)  
    - Santa Maria (Rio Grande do Sul)
- ✅ Traduzir coordenadas (latitude e longitude) para estado, região e cidade  
  Ex: `LATITUDE: -27.5777`, `LONGITUDE: -48.5081` → Estado: SC, Cidade: Florianópolis
- ✅ Traduzir localização (estado e cidade) para coordenadas (latitude e longitude)  
  Ex: Estado: SC, Cidade: Florianópolis → `LATITUDE: -27.5777`, `LONGITUDE: -48.5081`
- ✅ Traduzir código do IBGE para coordenadas (latitude e longitude)  
  Ex: `4205407` → `LATITUDE: -27.5777`, `LONGITUDE: -48.5081`

---

**Contato:**  
📧 Email: [thiagoweiss007@gmail.com](mailto:thiagoweiss007@gmail.com)  
💻 GitHub: [Thiago-Weiss](https://github.com/Thiago-Weiss/Projeto-api-cidades)
""",
    version="1.0.0",
    contact={
        "name": "Thiago Weiss Silva",
        "email": "thiagoweiss007@gmail.com",
    }
)

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


