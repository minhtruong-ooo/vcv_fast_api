# app/models/epsta.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Epsta(Base):
    __table__ = Table(
        "epsta",
        Base.metadata,
        autoload_with=engine,   # DB-first reflection
        # schema="public",      # bật nếu bảng không ở public
    )
