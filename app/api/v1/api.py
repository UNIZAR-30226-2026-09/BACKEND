from fastapi import APIRouter
from app.core.map_state import game_map_state
from app.schemas.map import MapDataSchema

# =============================================================================
# ROUTER PRINCIPAL (V1)
# =============================================================================
api_router = APIRouter()

@api_router.get("/status", tags=["Sistema"])
async def check_api_status():
    """Health Check para Docker"""
    return {"status": "ok", "version": "v1", "project": "SOBERANIA"}

@api_router.get("/map", response_model=MapDataSchema, tags=["Map"])
async def get_map_topology():
    """
    Devuelve la topología estática del mapa (Regiones, Comarcas y Adyacencias).
    El Frontend debe consumir esto una sola vez al iniciar la aplicación.
    """
    return game_map_state