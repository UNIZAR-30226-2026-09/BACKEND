from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from app.db.base import Base

class User(Base):
    __tablename__ = "usuarios"

    username: Mapped[str] = mapped_column(String(50), primary_key=True)
    password: Mapped[str] = mapped_column()