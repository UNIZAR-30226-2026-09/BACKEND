from fastapi import APIRouter

# =============================================================================
# ROUTER PRINCIPAL (V1)
# =============================================================================
api_router = APIRouter()

@api_router.get("/status", tags=["Sistema"])
async def check_api_status():
    """Health Check para Docker"""
    return {"status": "ok", "version": "v1", "project": "SOBERANIA"}