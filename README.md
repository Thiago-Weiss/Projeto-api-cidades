# 📍 Brasil GeoAPI

**Brasil GeoAPI** é uma API desenvolvida em **Python** utilizando **FastAPI** e **Pandas**, que fornece dados geográficos do Brasil.  
Com ela, é possível consultar estados, cidades, bairros, traduzir códigos do IBGE em localizações, além de buscar nomes para encontrar locais correspondentes.

---

## 🚀 Funcionalidades

✅ Listar todos os **estados** do Brasil  
✅ Listar **cidades** de um estado  
✅ Listar **bairros** de uma cidade  
✅ Traduzir **códigos IBGE** para nomes de localizações  
✅ Buscar por **nomes** para ver possíveis locais correspondentes  

---

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)  
- [FastAPI](https://fastapi.tiangolo.com/)  
- [Pandas](https://pandas.pydata.org/)  
- [Uvicorn](https://www.uvicorn.org/) (para rodar o servidor)

---

## 📂 Estrutura do projeto
app/
├── main.py # Inicializa a API FastAPI
├── api/ # Rotas da API
├── core/ # Constantes, schemas e configs
├── data/ # Dados em Parquet
├── services/ # Serviços e funções auxiliares
└── requirements.txt # Dependências do projeto

## ▶️ Como rodar o projeto localmente

1️⃣ **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/brasil-geoapi.git
cd brasil-geoapi
```

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt

uvicorn app.main:app --reload

http://127.0.0.1:8000/docs




📊 Exemplos de uso
Buscar todos os estados

bash
Copiar
Editar
GET /estados
Buscar cidades de um estado

bash
Copiar
Editar
GET /estados/{uf}/cidades
Buscar bairros de uma cidade

bash
Copiar
Editar
GET /cidades/{cidade}/bairros
Traduzir código IBGE para nome de localidade

bash
Copiar
Editar
GET /codigo/{codigo}
Buscar por nome

bash
Copiar
Editar
GET /buscar?nome=floresta
📜 Licença
Este projeto está sob a licença MIT. Você pode usá-lo, modificá-lo e distribuí-lo livremente.