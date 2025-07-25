from sqlalchemy import Column, Integer, String
from app.models.base import Base

class Sample(Base):
    __tablename__ = "sample_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)