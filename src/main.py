from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.database import get_db, engine
from src.models import User, Base

app = FastAPI()

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/usuarios")
async def obtener_usuarios(db: AsyncSession = Depends(get_db)):
    res = await db.execute(select(User))
    return res.scalars().all()

@app.post("/usuarios")
async def crear_usuario(username: str, passw: str, db: AsyncSession = Depends(get_db)):
    nuevo = User(username=username, password=passw)
    db.add(nuevo)
    await db.commit()
    return nuevo

@app.put("/usuarios/{username}")
async def editar_usuario(username: str, nueva_passw: str, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, username)
    user.password = nueva_passw
    await db.commit()
    return user

@app.delete("/usuarios/{username}")
async def borrar_usuario(username: str, db: AsyncSession = Depends(get_db)):
    user = await db.get(User, username)
    await db.delete(user)
    await db.commit()
    return {"status": "borrado"}