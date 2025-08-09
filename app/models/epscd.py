# app/models/epscd.py
from sqlalchemy import Table
from app.models.base import Base
from app.db.session import engine

class Epscd(Base):
    __table__ = Table(
        "epscd",
        Base.metadata,
        autoload_with=engine,
        # schema="public",  # nếu không ở public thì mở dòng này
    )
