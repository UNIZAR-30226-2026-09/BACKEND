import json
from pathlib import Path
from app.schemas.map import MapDataSchema

# Calculamos la ruta absoluta al archivo JSON para evitar problemas con Docker
DATA_PATH = Path(__file__).parent / "data" / "map_aragon.json"

def load_map_data() -> MapDataSchema:
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Esto valida el JSON contra el esquema. Si falta una coma o un campo, fallará al arrancar.
        return MapDataSchema(**data)
    except Exception as e:
        print(f"Error crítico cargando el mapa: {e}")
        raise e

# Variable global que actuará como nuestra caché en memoria.
# Se inicializa automáticamente cuando la aplicación arranca.
game_map_state: MapDataSchema = load_map_data()