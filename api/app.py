from fastapi import FastAPI
from api.routes import prices, health

app = FastAPI(
    title="Crypto Market Observer",
    description="API for fetching and analyzing cryptocurrency market data",
    version="1.0.0"
)

# Include routers
app.include_router(health.router)
app.include_router(prices.router, prefix="/api/prices", tags=["prices"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
