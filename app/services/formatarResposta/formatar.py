import pandas as pd
from app.core import RespostaFormato


def converter_para_o_front(df : pd.DataFrame, formato : RespostaFormato, remover_duplicados: bool = False) -> list:
    match formato:
        case RespostaFormato.LISTAS_DE_LISTAS:
            return [df.columns.tolist()] + df.values.tolist()
        
        case RespostaFormato.OBJETO:
            return df.to_dict(orient="records")
        
        case RespostaFormato.LISTAS:
            if remover_duplicados:
                return {col: df[col].unique().tolist() for col in df.columns}
            return {col: df[col].tolist() for col in df.columns}