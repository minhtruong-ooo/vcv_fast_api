from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Epscm(Base):
    __table__ = Table(
        "epscm",
        Base.metadata,
        autoload_with=engine,
        # schema="public",  # bật nếu bảng không ở public
    )