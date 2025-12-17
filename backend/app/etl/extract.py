import pandas as pd
from io import BytesIO

async def extract_from_upload(file):
    """Extrai dados de arquivo enviado"""
    contents = await file.read()
    
    if file.filename.endswith('.csv'):
        df = pd.read_csv(BytesIO(contents))
    elif file.filename.endswith(('.xlsx', '.xls')):
        df = pd.read_excel(BytesIO(contents))
    else:
        raise ValueError("Formato de arquivo não suportado")
    
    return df

def extract_from_database(query: str = None):
    """Extrai dados do banco de dados"""
    # Implementar conexão com DB
    pass
