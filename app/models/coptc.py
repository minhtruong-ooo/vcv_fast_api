# app/models/coptc.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Coptc(Base):
    __table__ = Table(
        "coptc",
        Base.metadata,
        autoload_with=engine,   # phản xạ toàn bộ cột/PK/FK từ DB
        # schema="public",      # bật nếu cần
    )