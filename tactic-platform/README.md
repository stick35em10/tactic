# TACTIC - Climate-Health Analytics Platform

🌍 Plataforma de análise integrada de dados climáticos e de saúde para Moçambique

## 📋 Pré-requisitos

- Docker & Docker Compose
- Git
- 4GB RAM mínimo
- 10GB espaço em disco

## 🚀 Quick Start

### 1. Clone o repositório
```bash
git clone <seu-repo>
cd tactic-platform
```

### 2. Configure variáveis de ambiente
```bash
cp .env.example .env
# Edite .env com suas configurações
```

### 3. Inicie os serviços
```bash
docker-compose up -d
```

### 4. Acesse a aplicação
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Database: localhost:5432

## 📦 Estrutura do Projeto

```
tactic-platform/
├── backend/              # FastAPI Backend
│   ├── app/
│   │   ├── etl/         # Pipeline ETL
│   │   ├── models/      # Modelos de dados
│   │   └── utils/       # Utilidades
│   └── Dockerfile
├── frontend/            # React Frontend
│   ├── src/
│   └── Dockerfile
├── database/            # PostgreSQL schemas
├── data/               # Dados
│   ├── raw/           # Dados brutos
│   ├── processed/     # Dados processados
│   └── outputs/       # Relatórios
└── docker-compose.yml
```

## 🔧 Comandos Úteis

### Ver logs
```bash
docker-compose logs -f
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Parar serviços
```bash
docker-compose down
```

### Rebuild containers
```bash
docker-compose up --build
```

### Executar testes
```bash
docker-compose exec backend pytest
```

### Acessar banco de dados
```bash
docker-compose exec db psql -U tactic_user -d tactic_db
```

## 📊 Funcionalidades

- ✅ Dashboard interativo com mapas
- ✅ Pipeline ETL completo
- ✅ Análise de correlação clima-saúde
- ✅ Gerador de dados sintéticos
- ✅ API REST documentada
- ✅ Validação e limpeza de dados
- ✅ Relatórios de qualidade

## 🌐 Deploy no Render

### Opção 1: Blueprint (Recomendado)
```bash
# Adicione render.yaml no root
render deploy
```

### Opção 2: Manual
1. Criar Web Service para backend
2. Criar Static Site para frontend
3. Criar PostgreSQL database
4. Configurar variáveis de ambiente

## 📝 API Endpoints

- `GET /` - Info da API
- `GET /health` - Health check
- `GET /api/provinces` - Lista províncias
- `GET /api/data/synthetic` - Gera dados sintéticos
- `POST /api/etl/upload` - Upload de dados
- `GET /api/analysis/summary` - Estatísticas

## 🔒 Segurança

- Nunca commite .env com senhas reais
- Use senhas fortes em produção
- Configure CORS adequadamente
- Use HTTPS em produção

## 📄 Licença

MIT License - TACTIC Project

## 👥 Equipe

Instituto Nacional de Saúde - Moçambique
Projeto TACTIC 2024-2025

## 📧 Contato

Para dúvidas e suporte, contacte a equipa TACTIC.
