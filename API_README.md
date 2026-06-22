# FastAPI Integration for Crypto Market Observer

## Project Structure

```
├── api/
│   ├── __init__.py
│   ├── app.py                 # FastAPI app instance & router setup
│   └── routes/
│       ├── __init__.py
│       ├── health.py          # Health check endpoint
│       └── prices.py          # Price fetching endpoints
├── py_code/
│   ├── __init__.py
│   ├── config.py              # Configuration & env variables
│   ├── database.py            # Database operations (psycopg2)
│   └── model.py               # ML models
├── main.py                    # CLI script (still works)
├── requirements.txt           # Dependencies
├── Dockerfile                 # Docker setup for FastAPI
└── docker-compose.yml         # Postgres + FastAPI services
```

## Setup Instructions

### Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   Create a `.env` file:
   ```
   COINGECKO_API_KEY=your_key_here
   DB_HOST=localhost
   DB_USER=user
   DB_PASS=password
   DB_NAME=crypto_db
   ```

3. **Start PostgreSQL (using Docker):**
   ```bash
   docker-compose up db
   ```

4. **Run the API:**
   ```bash
   uvicorn api.app:app --reload
   ```
   
   The API will be available at `http://localhost:8000`

### Docker Deployment

```bash
# Build and start both services
docker-compose up --build

# The API will be accessible at http://localhost:8000
```

## API Endpoints

### Health Check
- **GET** `/health`
  - Returns: `{"status": "ok", "message": "..."}`

### Fetch Prices
- **POST** `/api/prices/fetch`
  - Request body:
    ```json
    {
      "token_names": ["bitcoin", "ethereum"],
      "save_to_db": true
    }
    ```
  - Response: Price data with status

### Get Single Coin Price
- **GET** `/api/prices/{coin_name}`
  - Example: `GET /api/prices/bitcoin`
  - Response: Latest price for the coin

### Interactive API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Technology Stack

- **Framework**: FastAPI (async-ready, with validation)
- **Database**: PostgreSQL (with psycopg2 driver - unchanged)
- **Server**: Uvicorn (ASGI server)
- **Validation**: Pydantic models
- **HTTP Client**: Requests (for CoinGecko API)
- **ML**: LightGBM, XGBoost, scikit-learn

## Key Features

✅ **Keeps psycopg2** - No migration to SQLAlchemy needed  
✅ **Modular design** - Separate routes for different endpoints  
✅ **Error handling** - HTTP exceptions with proper status codes  
✅ **Docker ready** - Compose file for production setup  
✅ **Auto-documentation** - Swagger/ReDoc at `/docs` and `/redoc`  
✅ **Backward compatible** - CLI script still works  

## Notes

- The API keeps all original functionality from `main.py`
- Database operations use the existing `database.py` module
- All price fetching logic from `fetch_price()` is reused
- Docker setup includes volume persistence for PostgreSQL
