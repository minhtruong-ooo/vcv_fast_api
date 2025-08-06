# app/schemas/coptc.py
from typing import Optional
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, constr

# ---- Shared ----
class CoptcBase(BaseModel):
    tc003: Optional[constr(max_length=8)] = None
    tc004: Optional[constr(max_length=10)] = None
    tc005: Optional[constr(max_length=6)] = None
    tc006: Optional[constr(max_length=10)] = None
    tc007: Optional[constr(max_length=6)] = None
    tc008: Optional[constr(max_length=4)] = None
    tc009: Optional[Decimal] = None

    tc010: Optional[constr(max_length=72)] = None
    tc011: Optional[constr(max_length=72)] = None
    tc012: Optional[constr(max_length=20)] = None
    tc013: Optional[constr(max_length=16)] = None
    tc014: Optional[constr(max_length=16)] = None
    tc015: Optional[str] = None
    tc016: Optional[constr(max_length=1)] = None
    tc017: Optional[constr(max_length=20)] = None
    tc018: Optional[constr(max_length=30)] = None
    tc019: Optional[constr(max_length=1)] = None
    tc020: Optional[constr(max_length=20)] = None
    tc021: Optional[constr(max_length=20)] = None
    tc022: Optional[constr(max_length=10)] = None
    tc023: Optional[constr(max_length=10)] = None
    tc024: Optional[constr(max_length=10)] = None
    tc025: Optional[constr(max_length=10)] = None
    tc026: Optional[Decimal] = None
    tc027: Optional[constr(max_length=1)] = None
    tc028: Optional[int] = None
    tc029: Optional[Decimal] = None
    tc030: Optional[Decimal] = None
    tc031: Optional[Decimal] = None

    tc032: Optional[constr(max_length=10)] = None
    tc033: Optional[constr(max_length=10)] = None
    tc034: Optional[constr(max_length=4)] = None
    tc035: Optional[constr(max_length=20)] = None
    tc036: Optional[constr(max_length=10)] = None
    tc037: Optional[constr(max_length=255)] = None
    tc038: Optional[constr(max_length=255)] = None
    tc039: Optional[constr(max_length=8)] = None
    tc040: Optional[constr(max_length=10)] = None
    tc041: Optional[Decimal] = None
    tc042: Optional[constr(max_length=6)] = None
    tc043: Optional[Decimal] = None
    tc044: Optional[Decimal] = None
    tc045: Optional[Decimal] = None
    tc046: Optional[Decimal] = None
    tc047: Optional[constr(max_length=10)] = None
    tc048: Optional[constr(max_length=1)] = None
    tc049: Optional[constr(max_length=2)] = None
    tc050: Optional[constr(max_length=1)] = None
    tc051: Optional[constr(max_length=10)] = None

    tc052: Optional[constr(max_length=100)] = None
    tc053: Optional[constr(max_length=100)] = None
    tc054: Optional[constr(max_length=100)] = None
    tc055: Optional[constr(max_length=100)] = None
    tc056: Optional[constr(max_length=255)] = None
    tc057: Optional[constr(max_length=255)] = None
    tc058: Optional[int] = None
    tc059: Optional[constr(max_length=1)] = None
    tc060: Optional[constr(max_length=8)] = None
    tc061: Optional[constr(max_length=30)] = None
    tc062: Optional[Decimal] = None
    tc063: Optional[Decimal] = None
    tc064: Optional[Decimal] = None

    udf01: Optional[constr(max_length=60)] = None
    udf02: Optional[constr(max_length=60)] = None
    udf03: Optional[constr(max_length=60)] = None
    udf04: Optional[constr(max_length=60)] = None
    udf05: Optional[constr(max_length=60)] = None
    udf06: Optional[constr(max_length=60)] = None

    udf51: Optional[Decimal] = None
    udf52: Optional[Decimal] = None
    udf53: Optional[Decimal] = None
    udf54: Optional[Decimal] = None
    udf55: Optional[Decimal] = None
    udf56: Optional[Decimal] = None

    syncflag: Optional[int] = None
    syncdate: Optional[datetime] = None
    udf07: Optional[constr(max_length=60)] = None

class CoptcCreate(CoptcBase):
    tc001: constr(max_length=4)
    tc002: constr(max_length=11)

class CoptcUpdate(CoptcBase):
    pass  # tất cả đều optional

class CoptcOut(CoptcBase):
    tc001: str
    tc002: str

    class Config:
        from_attributes = True
