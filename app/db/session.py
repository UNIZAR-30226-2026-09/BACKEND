from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Motor de conexión asíncrono
engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=5,
    max_overflow=0,
    pool_pre_ping=True,
    echo=False
)

# Fábrica de sesiones
AsyncSessionLocal = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Dependencia para inyectar la sesión en los endpoints
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()