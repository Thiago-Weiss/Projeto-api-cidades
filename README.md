# 📍 Brasil GeoAPI

**Brasil GeoAPI** é uma API desenvolvida em **Python** utilizando **FastAPI** e **Pandas**, que fornece dados geográficos do Brasil.  
Com ela, é possível consultar estados, cidades, bairros, traduzir códigos do IBGE em localizações, além de buscar nomes para encontrar locais correspondentes.

---

## 🚀 Funcionalidades

✅ Listar todos os **estados** do Brasil  
✅ Listar **cidades** de um estado  
✅ Listar **bairros** de uma cidade  
✅ Traduzir **códigos IBGE** para localizações exp: 42 -> Santa Catarina   
✅ Buscar por **nomes** para ver possíveis locais correspondentes exp: pesquisando o nome **Santa Maria** na opcao de cidades vai retornar que tem duas cidades com esse nome uma em Rio Grande do Norte e a outra no Rio Grande do Sul

---

## 🛠️ Principais Tecnologias utilizadas

- [Python] Linguagem de programaçao
- [FastAPI] Fazer o Back End
- [Pandas] Trabalhar com os dados
- [Uvicorn] para rodar o servidor

---

## 📂 Estrutura do projeto
app/  
├── main.py # Inicializa a API FastAPI  
├── obterDados.py # Processa os dados brutos do IBGE  
├── api/ # Rotas da API  
├── core/ # Constantes, schemas e configs  
├── data/ # Dados em Parquet  
├── services/ # Serviços e funções auxiliares  
└── requirements.txt # Dependências do projeto  


## 📊 Rotas
![](img/docs.png)

### GET /estados
![](img/estados.png)

### GET /cidades
![](img/cidades.png)

### GET /bairros
![](img/bairros.png)

### GET /localizar-codigo/{codigo}
![](img/codigos.png)

### GET /localizar-nome/{nome}
![](img/nomes.png)


## ▶️ Como rodar o projeto localmente

1️⃣ **Clone o repositório**
```bash
https://github.com/seu-usuario/brasil-geoapi.git
```

```bash
https://github.com/seu-usuario/brasil-geoapi.git
```
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
```bash
pip install -r requirements.txt
```
```bash
uvicorn app.main:app --reload
ou
python -m uvicorn app.main:app --reload
```
acesse
```bash
http://127.0.0.1:8000/docs
```



📜 Licença
Este projeto está sob a licença MIT. Você pode usá-lo, modificá-lo e distribuí-lo livremente.

