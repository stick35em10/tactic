import pandas as pd
from sqlalchemy import create_engine, text
import os

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set.")

engine = create_engine(DATABASE_URL)

def save_to_database(df: pd.DataFrame, table_name: str = 'climate_health_data'):
    """Salva dados no banco de dados"""
    if df.empty:
        print("✓ DataFrame vazio, nenhum dado para salvar.")
        return 0

    try:
        # Usar 'append' para adicionar novos registros.
        # index=False para não salvar o índice do DataFrame como coluna.
        # if_exists='append' adiciona novas linhas.
        # Para evitar duplicatas na coluna (data, provincia), a tabela no DB deve ter uma restrição UNIQUE.
        df.to_sql(table_name, engine, if_exists='append', index=False, method='multi')
        print(f"✓ Dados salvos: {len(df)} registros na tabela {table_name}")
        return len(df)
    except Exception as e:
        print(f"Erro ao salvar dados no banco de dados: {e}")
        raise

def load_from_database(query: str = "SELECT * FROM climate_health_data") -> pd.DataFrame:
    """Carrega dados do banco de dados"""
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(query), connection)
        print(f"✓ Dados carregados: {len(df)} registros")
        return df
    except Exception as e:
        print(f"Erro ao carregar dados do banco de dados: {e}")
        raise
