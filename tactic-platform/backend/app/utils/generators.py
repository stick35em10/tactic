import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class MozambiqueDataGenerator:
    def __init__(self):
        self.provinces = [
            'Maputo', 'Gaza', 'Inhambane', 'Sofala', 'Manica',
            'Tete', 'Zambézia', 'Nampula', 'Cabo Delgado', 'Niassa'
        ]
        
        self.coastal_provinces = [
            'Maputo', 'Gaza', 'Inhambane', 'Sofala',
            'Zambézia', 'Nampula', 'Cabo Delgado'
        ]
    
    def generate_climate_health_data(self, n_rows: int = 1000) -> pd.DataFrame:
        """Gera dados sintéticos realistas para Moçambique"""
        np.random.seed(42)
        
        data = []
        start_date = datetime(2023, 1, 1)
        
        for i in range(n_rows):
            province = np.random.choice(self.provinces)
            date = start_date + timedelta(days=np.random.randint(0, 730))
            
            is_coastal = province in self.coastal_provinces
            is_rainy_season = date.month in [10, 11, 12, 1, 2, 3]
            
            # Clima
            temp_base = 26 if is_coastal else 24
            temp_variation = 4 if is_rainy_season else 2
            temperatura = np.random.normal(temp_base, temp_variation)
            temperatura = np.clip(temperatura, 18, 35)
            
            precip_base = 150 if is_rainy_season else 30
            precipitacao = np.random.gamma(2, precip_base/2)
            if not is_rainy_season:
                precipitacao *= 0.3
            
            # Casos de saúde (correlacionados com clima)
            malaria = int(max(0, np.random.poisson(
                50 + temperatura * 10 + precipitacao * 0.5
            )))
            
            diarreia = int(max(0, np.random.poisson(
                30 + precipitacao * 0.3 + temperatura * 3
            )))
            
            renal = int(max(0, np.random.poisson(
                20 + (temperatura - 25) * 2
            )))
            
            mental = int(max(0, np.random.poisson(
                40 + (temperatura - 22) * 1.5
            )))
            
            data.append({
                'data': date,
                'provincia': province,
                'temperatura': round(temperatura, 1),
                'precipitacao': round(precipitacao, 0),
                'casos_malaria': malaria,
                'casos_diarreia': diarreia,
                'casos_renais': renal,
                'casos_saude_mental': mental,
                'populacao': np.random.randint(800000, 2500000),
                'epoca': 'Chuvosa' if is_rainy_season else 'Seca'
            })
        
        df = pd.DataFrame(data)
        df = df.sort_values(['provincia', 'data']).reset_index(drop=True)
        
        return df
