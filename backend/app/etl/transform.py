import pandas as pd
import numpy as np
from datetime import datetime

class DataTransformer:
    def __init__(self):
        self.required_columns = [
            'data', 'provincia', 'temperatura', 'precipitacao',
            'casos_malaria', 'casos_diarreia'
        ]
    
    def clean_and_harmonize(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pipeline completo de limpeza e harmonização"""
        df = df.copy()
        
        # 1. Remover duplicatas
        df = self._remove_duplicates(df)
        
        # 2. Padronizar nomes de colunas
        df = self._standardize_columns(df)
        
        # 3. Tratar valores ausentes
        df = self._handle_missing_values(df)
        
        # 4. Validar e corrigir outliers
        df = self._handle_outliers(df)
        
        # 5. Padronizar formatos
        df = self._standardize_formats(df)
        
        # 6. Criar variáveis derivadas
        df = self._create_derived_variables(df)
        
        return df
    
    def _remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        initial_rows = len(df)
        df = df.drop_duplicates(subset=['data', 'provincia'], keep='first')
        print(f"✓ Duplicatas removidas: {initial_rows - len(df)}")
        return df
    
    def _standardize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        column_mapping = {
            'date': 'data',
            'province': 'provincia',
            'temp': 'temperatura',
            'temperature': 'temperatura',
            'rainfall': 'precipitacao',
            'malaria_cases': 'casos_malaria',
            'diarrhea_cases': 'casos_diarreia'
        }
        df = df.rename(columns=column_mapping)
        return df
    
    def _handle_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        # Temperatura: interpolação
        if 'temperatura' in df.columns:
            df['temperatura'] = df.groupby('provincia')['temperatura'].transform(
                lambda x: x.interpolate(method='linear', limit_direction='both')
            )
        
        # Casos: preencher com 0
        case_columns = [col for col in df.columns if 'casos_' in col]
        df[case_columns] = df[case_columns].fillna(0)
        
        return df
    
    def _handle_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            df[col] = df[col].clip(lower, upper)
        
        return df
    
    def _standardize_formats(self, df: pd.DataFrame) -> pd.DataFrame:
        if 'data' in df.columns:
            df['data'] = pd.to_datetime(df['data'])
            df['ano'] = df['data'].dt.year
            df['mes'] = df['data'].dt.month
        
        if 'provincia' in df.columns:
            df['provincia'] = df['provincia'].str.title()
        
        return df
    
    def _create_derived_variables(self, df: pd.DataFrame) -> pd.DataFrame:
        case_cols = [col for col in df.columns if 'casos_' in col]
        if case_cols:
            df['casos_total'] = df[case_cols].sum(axis=1)
        
        if 'mes' in df.columns:
            df['epoca'] = df['mes'].apply(
                lambda x: 'Chuvosa' if x in [10,11,12,1,2,3] else 'Seca'
            )
        
        return df

def clean_and_harmonize(df: pd.DataFrame) -> pd.DataFrame:
    transformer = DataTransformer()
    return transformer.clean_and_harmonize(df)
