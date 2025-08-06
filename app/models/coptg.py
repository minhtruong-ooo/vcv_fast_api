# app/models/coptg.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Coptg(Base):
    __table__ = Table(
        "coptg",
        Base.metadata,
        autoload_with=engine,   # DB-first reflection
        # schema="public",      # chỉnh nếu không phải public
    )
