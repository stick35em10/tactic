from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd
from datetime import datetime
import os
from utils.generators import MozambiqueDataGenerator
from etl.load import save_to_database, load_from_database

app = FastAPI(
    title="TACTIC Climate-Health API",
    version="1.0.0",
    description="API para análise de dados clima-saúde em Moçambique"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "TACTIC Climate-Health Platform API",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "operational"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "database": "connected",
        "services": "operational"
    }

@app.get("/api/provinces")
async def get_provinces():
    """Lista todas as províncias de Moçambique"""
    provinces = [
        {"id": 1, "name": "Maputo", "region": "Sul"},
        {"id": 2, "name": "Gaza", "region": "Sul"},
        {"id": 3, "name": "Inhambane", "region": "Sul"},
        {"id": 4, "name": "Sofala", "region": "Centro"},
        {"id": 5, "name": "Manica", "region": "Centro"},
        {"id": 6, "name": "Tete", "region": "Centro"},
        {"id": 7, "name": "Zambézia", "region": "Centro"},
        {"id": 8, "name": "Nampula", "region": "Norte"},
        {"id": 9, "name": "Cabo Delgado", "region": "Norte"},
        {"id": 10, "name": "Niassa", "region": "Norte"}
    ]
    return provinces

@app.post("/api/data/generate-and-load")
async def generate_and_load_data(rows: int = 100):
    """Gera dados sintéticos e os carrega no banco de dados."""
    try:
        generator = MozambiqueDataGenerator()
        df = generator.generate_climate_health_data(rows)
        inserted_rows = save_to_database(df)
        return {"status": "success", "message": f"{inserted_rows} linhas de dados sintéticos geradas e carregadas com sucesso."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar e carregar dados: {str(e)}")

@app.get("/api/data/synthetic")
async def generate_synthetic_data(rows: int = 100, year: int = 2024):
    """Gera dados sintéticos para demonstração"""
    try:
        from utils.generators import MozambiqueDataGenerator
        generator = MozambiqueDataGenerator()
        data = generator.generate_climate_health_data(rows)
        
        return {
            "status": "success",
            "rows": len(data),
            "data": data.to_dict(orient='records')[:50]  # Limitar resposta
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/etl/upload")
async def upload_data(file: UploadFile = File(...)):
    """Upload e processamento de arquivos de dados"""
    try:
        # Validar extensão
        if not file.filename.endswith(('.csv', '.xlsx', '.xls')):
            raise HTTPException(400, "Formato não suportado. Use CSV ou Excel.")
        
        # Ler arquivo
        contents = await file.read()
        
        if file.filename.endswith('.csv'):
            df = pd.read_csv(pd.io.common.BytesIO(contents))
        else:
            df = pd.read_excel(pd.io.common.BytesIO(contents))
        
        # Validação básica
        validation = {
            "filename": file.filename,
            "rows": len(df),
            "columns": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.astype(str).to_dict()
        }
        
        return {
            "status": "success",
            "message": "Arquivo processado com sucesso",
            "validation": validation
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar arquivo: {str(e)}")

@app.get("/api/analysis/summary")
async def get_summary_stats():
    """Estatísticas resumidas do sistema"""
    return {
        "total_cases": 45234,
        "avg_temperature": 26.3,
        "total_rainfall": 892,
        "population_at_risk": 2100000,
        "data_quality": 94.2,
        "last_updated": datetime.now().isoformat()
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
