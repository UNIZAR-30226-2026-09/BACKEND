from pydantic import BaseModel
from typing import List, Dict

class MapMetadataSchema(BaseModel):
    version: str
    name: str
    total_comarcas: int

class RegionSchema(BaseModel):
    name: str
    bonus_troops: int
    comarcas: List[str]

class ComarcaSchema(BaseModel):
    name: str
    region_id: str
    adjacent_to: List[str]

class MapDataSchema(BaseModel):
    metadata: MapMetadataSchema
    regions: Dict[str, RegionSchema]
    comarcas: Dict[str, ComarcaSchema]