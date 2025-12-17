-- TACTIC Database Initialization

CREATE TABLE IF NOT EXISTS climate_health_data (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    provincia VARCHAR(100) NOT NULL,
    temperatura DECIMAL(5,2),
    precipitacao DECIMAL(7,2),
    casos_malaria INTEGER DEFAULT 0,
    casos_diarreia INTEGER DEFAULT 0,
    casos_renais INTEGER DEFAULT 0,
    casos_saude_mental INTEGER DEFAULT 0,
    populacao INTEGER,
    epoca VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(data, provincia)
);

CREATE INDEX idx_data ON climate_health_data(data);
CREATE INDEX idx_provincia ON climate_health_data(provincia);
CREATE INDEX idx_epoca ON climate_health_data(epoca);

-- Tabela de metadados
CREATE TABLE IF NOT EXISTS data_metadata (
    id SERIAL PRIMARY KEY,
    dataset_name VARCHAR(255),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_records INTEGER,
    data_quality_score DECIMAL(5,2),
    notes TEXT
);

COMMENT ON TABLE climate_health_data IS 'Dados integrados de clima e saúde para Moçambique';
