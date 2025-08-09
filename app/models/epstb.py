# app/models/epstb.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Epstb(Base):
    __table__ = Table(
        "epstb",
        Base.metadata,
        autoload_with=engine,   # DB-first
        # schema="public",      # chỉnh nếu khác
    )