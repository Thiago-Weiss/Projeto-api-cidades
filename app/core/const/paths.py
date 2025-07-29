from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = "data"

CIDADE_ESTADOS_ARQUIVO_ORIGINAL = BASE_DIR / DATA_DIR / "dadosBrutos.ods"
CIDADE_ESTADOS_ARQUIVO = BASE_DIR / DATA_DIR / "cidadeEstados.parquet"


