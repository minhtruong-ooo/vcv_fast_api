# app/models/coptd.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Coptd(Base):
    __table__ = Table(
        "coptd",
        Base.metadata,
        autoload_with=engine,   # phản xạ toàn bộ cột/PK/FK từ DB
        # schema="public",      # đổi nếu bảng không ở public
    )