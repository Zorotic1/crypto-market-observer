from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sys
from pathlib import Path

# Add current directory to path to import main
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from main import fetch_price
from py_code.database import save_to_db

router = APIRouter()

class PriceRequest(BaseModel):
    token_names: List[str]
    save_to_db: Optional[bool] = True

class PriceResponse(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[dict] = None

@router.post("/fetch", response_model=PriceResponse)
def fetch_prices(request: PriceRequest):
    """
    Fetch cryptocurrency prices from CoinGecko API
    
    - **token_names**: List of crypto names (e.g., ["bitcoin", "ethereum"])
    - **save_to_db**: Whether to save results to database (default: True)
    """
    try:
        # Validate input
        if not request.token_names or len(request.token_names) == 0:
            raise HTTPException(status_code=400, detail="token_names cannot be empty")
        
        # Fetch prices
        results = fetch_price(request.token_names)
        
        if results is None:
            raise HTTPException(
                status_code=503,
                detail="Failed to fetch prices from CoinGecko API. Please try again later."
            )
        
        # Save to database if requested
        if request.save_to_db:
            try:
                save_to_db(results, request.token_names)
                message = "Prices fetched and saved to database successfully"
            except Exception as db_error:
                message = f"Prices fetched but database save failed: {str(db_error)}"
        else:
            message = "Prices fetched successfully (not saved to database)"
        
        return PriceResponse(
            status="success",
            message=message,
            data=results
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.get("/{coin_name}")
def get_coin_price(coin_name: str):
    """
    Get current price for a specific cryptocurrency
    
    - **coin_name**: Crypto name (e.g., "bitcoin", "ethereum")
    """
    try:
        results = fetch_price([coin_name])
        
        if results is None:
            raise HTTPException(
                status_code=503,
                detail=f"Failed to fetch price for {coin_name}"
            )
        
        return {
            "status": "success",
            "coin": coin_name,
            "data": results[0] if results else None
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
