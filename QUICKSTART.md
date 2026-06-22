# 🚀 Quick Start - FastAPI Integration Complete!

## ✅ Setup Complete

Your project now has a full FastAPI integration with psycopg2! Here's what was added:

### New Files Created
```
api/
├── __init__.py
├── app.py                    # FastAPI app with route setup
└── routes/
    ├── __init__.py
    ├── health.py             # GET /health
    └── prices.py             # POST /api/prices/fetch, GET /api/prices/{coin}

py_code/__init__.py           # Makes py_code a package

API_README.md                 # Full API documentation
QUICKSTART.md                 # This file
```

### Updated Files
- ✏️ `requirements.txt` - Added fastapi, uvicorn, pydantic
- ✏️ `Dockerfile` - Now runs uvicorn instead of main.py
- ✏️ `docker-compose.yml` - Added port 8000, volume persistence, reload mode
- ✏️ `main.py` - Refactored to be importable as a module

## 🎯 Run the API Locally

### 1. Install Dependencies (one-time)
```bash
pip install -r requirements.txt
```

### 2. Start PostgreSQL (required for database operations)
```bash
docker-compose up db
```

### 3. Run the API
```bash
uvicorn api.app:app --reload
```

The API will be available at: **http://localhost:8000**

## 📚 API Endpoints

### Health Check
```bash
curl http://localhost:8000/health
```

### Fetch Cryptocurrency Prices
```bash
curl -X POST http://localhost:8000/api/prices/fetch \
  -H "Content-Type: application/json" \
  -d '{
    "token_names": ["bitcoin", "ethereum"],
    "save_to_db": true
  }'
```

### Get Single Coin Price
```bash
curl http://localhost:8000/api/prices/bitcoin
```

### View API Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🐳 Run with Docker Compose

```bash
# Start everything (FastAPI + PostgreSQL)
docker-compose up --build

# API will be at http://localhost:8000
# Database at localhost:5432
```

## 📝 Environment Variables

Create a `.env` file:
```
COINGECKO_API_KEY=your_api_key_here
DB_HOST=localhost
DB_USER=user
DB_PASS=password
DB_NAME=crypto_db
```

## 🔍 Key Features

✅ **Keeps psycopg2** - No SQLAlchemy migration needed  
✅ **Type Validation** - Pydantic models for request/response validation  
✅ **Error Handling** - Proper HTTP status codes and error messages  
✅ **Auto Documentation** - Interactive API docs at /docs  
✅ **Modular Design** - Separate routes for scalability  
✅ **Docker Ready** - Production-ready docker-compose setup  
✅ **CLI Compatible** - `python main.py` still works  

## 📊 Architecture

```
┌─────────────────┐
│   FastAPI       │
│   (API Layer)   │
└────────┬────────┘
         │
    ┌────┴────┐
    │          │
┌───▼──────┐  ┌─▼──────────┐
│  main.py │  │ py_code/   │
│(Reused)  │  │ - config   │
└──────────┘  │ - database │
              │ - models   │
              └────────────┘
                    │
              ┌─────▼──────┐
              │ PostgreSQL │
              │  (psycopg2)│
              └────────────┘
```

## 🐛 Troubleshooting

**ModuleNotFoundError when running API?**
- Make sure you're in the project root directory
- Install requirements: `pip install -r requirements.txt`

**Database connection errors?**
- Ensure PostgreSQL is running: `docker-compose up db`
- Check .env has correct DB credentials

**Port 8000 already in use?**
- Change port: `uvicorn api.app:app --port 8001`

## 📚 Next Steps

1. **Add more endpoints** - Extend `api/routes/prices.py`
2. **Add authentication** - Use FastAPI's security features
3. **Add ML predictions** - Create `api/routes/predictions.py` using `py_code/model.py`
4. **Deploy to production** - Use docker-compose with proper env vars

## 💡 Example: Adding a New Endpoint

Add this to `api/routes/prices.py`:

```python
@router.get("/stats/{coin_name}")
def get_coin_stats(coin_name: str):
    """Get stats for a coin"""
    results = fetch_price([coin_name])
    if results:
        return results[0]
    return {"error": "Coin not found"}
```

Then restart the API - it's automatically available at `/api/prices/stats/{coin_name}`!

---

**Questions?** Check `API_README.md` for detailed documentation!
