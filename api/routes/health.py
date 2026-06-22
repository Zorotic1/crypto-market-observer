from fastapi import APIRouter

router = APIRouter()

@router.get("/health", tags=["health"])
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "message": "Crypto Market Observer API is running"}
