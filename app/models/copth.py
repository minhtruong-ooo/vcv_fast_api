# app/models/copth.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Copth(Base):
    __table__ = Table(
        "copth",
        Base.metadata,
        autoload_with=engine,   # DB-first reflection
        # schema="public",      # đổi nếu không ở public
    )