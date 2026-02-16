from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings 

# Asincrono con pool fijo
engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=5,            # 5 conexiones
    max_overflow=0,         
    pool_pre_ping=True,      
    echo=False              # = True imprime logs de SQL
)

# Genera conexiones de 'engine' asincronas 
AsyncSessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# Pedir acceso a BD
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()