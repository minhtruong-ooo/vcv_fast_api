from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class CoptdBase(BaseModel):
    # (giữ NGUYÊN toàn bộ các field bạn đã khai báo)
    td004: Optional[constr(max_length=20)] = None
    td005: Optional[constr(max_length=60)] = None
    td006: Optional[constr(max_length=60)] = None
    td007: Optional[constr(max_length=10)] = None
    td008: Optional[Decimal] = None
    td009: Optional[Decimal] = None
    td010: Optional[constr(max_length=4)] = None
    td011: Optional[Decimal] = None
    td012: Optional[Decimal] = None
    td013: Optional[constr(max_length=8)] = None
    td014: Optional[constr(max_length=50)] = None
    td015: Optional[constr(max_length=11)] = None
    td016: Optional[constr(max_length=1)] = None
    td017: Optional[constr(max_length=4)] = None
    td018: Optional[constr(max_length=11)] = None
    td019: Optional[constr(max_length=4)] = None
    td020: Optional[constr(max_length=255)] = None
    td021: Optional[constr(max_length=1)] = None
    td022: Optional[Decimal] = None
    td023: Optional[constr(max_length=4)] = None
    td024: Optional[Decimal] = None
    td025: Optional[Decimal] = None
    td026: Optional[Decimal] = None
    td027: Optional[constr(max_length=20)] = None
    td028: Optional[constr(max_length=4)] = None
    td029: Optional[constr(max_length=3)] = None
    td030: Optional[Decimal] = None
    td031: Optional[Decimal] = None
    td032: Optional[Decimal] = None
    td033: Optional[Decimal] = None
    td034: Optional[Decimal] = None
    td035: Optional[Decimal] = None
    td036: Optional[constr(max_length=4)] = None
    td037: Optional[Decimal] = None
    td038: Optional[Decimal] = None
    td039: Optional[Decimal] = None
    td040: Optional[Decimal] = None
    td041: Optional[Decimal] = None
    td042: Optional[Decimal] = None
    td043: Optional[Decimal] = None
    td044: Optional[Decimal] = None
    td045: Optional[Decimal] = None
    td046: Optional[constr(max_length=10)] = None
    td047: Optional[constr(max_length=1)] = None
    td048: Optional[constr(max_length=8)] = None
    td049: Optional[constr(max_length=30)] = None
    td050: Optional[Decimal] = None
    td051: Optional[Decimal] = None
    td052: Optional[Decimal] = None
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
    td200: Optional[constr(max_length=30)] = None
    td201: Optional[constr(max_length=200)] = None
    td202: Optional[constr(max_length=50)] = None
    td203: Optional[datetime] = None
    td204: Optional[datetime] = None
    td205: Optional[constr(max_length=255)] = None
    td206: Optional[constr(max_length=8)] = None
    td207: Optional[datetime] = None
    td208: Optional[datetime] = None
    td209: Optional[constr(max_length=255)] = None
    td210: Optional[constr(max_length=255)] = None
    td211: Optional[constr(max_length=255)] = None
    td212: Optional[datetime] = None
    td213: Optional[constr(max_length=100)] = None
    td214: Optional[constr(max_length=60)] = None
    syncflag: Optional[int] = None
    syncdate: Optional[datetime] = None
    td215: Optional[constr(max_length=1)] = None
    td216: Optional[constr(max_length=1)] = None
    td217: Optional[constr(max_length=1)] = None
    td218: Optional[constr(max_length=10)] = None
    td219: Optional[Decimal] = None
    td220: Optional[constr(max_length=30)] = None
    td221: Optional[constr(max_length=50)] = None
    td222: Optional[constr(max_length=50)] = None
    udf57: Optional[constr(max_length=2)] = None
    udf58: Optional[constr(max_length=2)] = None
    udf59: Optional[constr(max_length=50)] = None
    company: Optional[constr(max_length=10)] = None
    creator: Optional[constr(max_length=10)] = None
    usr_group: Optional[constr(max_length=10)] = None
    create_date: Optional[constr(max_length=17)] = None
    modifier: Optional[constr(max_length=10)] = None
    modi_date: Optional[constr(max_length=17)] = None
    flag: Optional[Decimal] = None
    td223: Optional[constr(max_length=50)] = None
    td224: Optional[constr(max_length=50)] = None
    td225: Optional[Decimal] = None
    td226: Optional[int] = None
    td227: Optional[constr(max_length=1)] = None
    td228: Optional[constr(max_length=1)] = None
    td229: Optional[constr(max_length=1)] = None
    td230: Optional[int] = None
    td231: Optional[int] = None
    beensynced: Optional[constr(max_length=100)] = None
    td053: Optional[constr(max_length=1)] = None
    udf60: Optional[Decimal] = None
    td232: Optional[Decimal] = None

class CoptdCreate(InBase, CoptdBase):
    td001: constr(max_length=4)
    td002: constr(max_length=11)
    td003: constr(max_length=4)

class CoptdUpdate(InBase, CoptdBase):
    pass

class CoptdOut(OutBase, CoptdBase):
    td001: str
    td002: str
    td003: str
    model_config = ConfigDict(from_attributes=True)
