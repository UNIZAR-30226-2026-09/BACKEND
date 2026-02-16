# Backend
Servidor con FastAPI y Python 3.12.

## Gestión de librerías (`uv)

Usamos `uv` para que las versiones sean idénticas en todas las máquinas.

**Sólo hay que instalarse `uv`si se van a gestionar librerias. Si solo se programa API o lógica de juego no es necesario**


### Uso de UV:
1. **Instalar uv**: 
   - Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - macOS/Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. **Añadir librería**: `uv add nombre-libreria` (esto actualizará el `uv.lock`).
3. **Sincronizar local**: `uv sync`.

**Nota**: Cada vez que se actualice el archivo `uv.lock` en el repositorio (cuando alguien añada una nueva libreria), todos los demás desarrolladores deben hacer un `docker compose up --build` para actualizar sus contenedores.