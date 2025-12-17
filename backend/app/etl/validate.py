import pandas as pd

def validate_data(df: pd.DataFrame) -> dict:
    """Valida qualidade e integridade dos dados"""
    
    validation_report = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'stats': {}
    }
    
    # Verificar dados vazios
    if df.empty:
        validation_report['valid'] = False
        validation_report['errors'].append("DataFrame está vazio")
        return validation_report
    
    # Verificar valores ausentes
    missing_pct = (df.isnull().sum() / len(df) * 100).to_dict()
    validation_report['stats']['missing_values'] = missing_pct
    
    for col, pct in missing_pct.items():
        if pct > 50:
            validation_report['warnings'].append(
                f"Coluna '{col}' tem {pct:.1f}% de valores ausentes"
            )
    
    # Verificar duplicatas
    duplicates = df.duplicated().sum()
    validation_report['stats']['duplicates'] = int(duplicates)
    
    if duplicates > 0:
        validation_report['warnings'].append(
            f"Encontradas {duplicates} linhas duplicadas"
        )
    
    # Estatísticas gerais
    validation_report['stats']['total_rows'] = len(df)
    validation_report['stats']['total_columns'] = len(df.columns)
    validation_report['stats']['completeness'] = round(
        100 - (df.isnull().sum().sum() / (len(df) * len(df.columns)) * 100), 2
    )
    
    return validation_report
