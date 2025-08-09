# app/schemas/epscd.py
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class EpscdBase(BaseModel):
    # CD004..CD043 (PK để ở Create/Out)
    cd004: Optional[constr(max_length=4)] = None    # 訂單單別
    cd005: Optional[constr(max_length=11)] = None   # 訂單單號
    cd006: Optional[constr(max_length=4)] = None    # 訂單序號
    cd007: Optional[constr(max_length=16)] = None   # 品號
    cd008: Optional[Decimal] = None                 # 出貨數量 (N 9)
    cd009: Optional[constr(max_length=1)] = None    # 審核碼
    cd010: Optional[constr(max_length=10)] = None   # 出貨倉庫
    cd011: Optional[Decimal] = None                 # 出貨數量 (N 9)
    cd012: Optional[constr(max_length=4)] = None    # 出貨通知單別
    cd013: Optional[constr(max_length=11)] = None   # 出貨通知單號
    cd014: Optional[constr(max_length=4)] = None    # 出貨序號
    cd015: Optional[constr(max_length=1)] = None    # 包裝方式
    cd016: Optional[Decimal] = None                 # 包裝數量 (N 9)
    cd017: Optional[Decimal] = None                 # 毛重 (N 9)
    cd018: Optional[Decimal] = None                 # 淨重 (N 9)
    cd019: Optional[constr(max_length=1)] = None    # 更新碼
    cd020: Optional[Decimal] = None                 # 材積 (N 9)
    cd021: Optional[Decimal] = None                 # 長 (N 9)
    cd022: Optional[Decimal] = None                 # 寬 (N 9)
    cd023: Optional[Decimal] = None                 # 高 (N 9)
    cd024: Optional[Decimal] = None                 # CBM (N 9)
    cd025: Optional[constr(max_length=10)] = None   # 客戶
    cd026: Optional[constr(max_length=10)] = None   # P-O
    cd027: Optional[constr(max_length=10)] = None   # 客號
    cd028: Optional[Decimal] = None                 # 箱數 (N 9)
    cd029: Optional[Decimal] = None                 # 總數 (N 9)
    cd030: Optional[Decimal] = None                 # 訂單數量 (N 9)
    cd031: Optional[Decimal] = None                 # 訂單欠數 (N 9)
    cd032: Optional[Decimal] = None                 # 已出貨數量 (N 9)
    cd033: Optional[Decimal] = None                 # 總毛重 (N 9)
    cd034: Optional[Decimal] = None                 # 總淨重 (N 9)
    cd035: Optional[constr(max_length=50)] = None   # 備注
    cd036: Optional[Decimal] = None                 # 預留字段 (N 9)
    cd037: Optional[Decimal] = None                 # 預留字段 (N 9)
    cd038: Optional[constr(max_length=9)] = None    # 出貨工廠 (V 9)
    cd039: Optional[constr(max_length=20)] = None   # 產品類別
    cd040: Optional[constr(max_length=20)] = None   # SKU號碼
    cd041: Optional[constr(max_length=20)] = None   # 顏色碼
    cd042: Optional[constr(max_length=10)] = None   # 包裝類型
    cd043: Optional[constr(max_length=60)] = None   # 包裝方式(分裝套裝)

class EpscdCreate(InBase, EpscdBase):
    cd001: constr(max_length=4)      # 報關單單別
    cd002: constr(max_length=11)     # 報關單號
    cd003: constr(max_length=4)      # 序號

class EpscdUpdate(InBase, EpscdBase):
    pass

class EpscdOut(OutBase, EpscdBase):
    cd001: str
    cd002: str
    cd003: str
    model_config = ConfigDict(from_attributes=True)