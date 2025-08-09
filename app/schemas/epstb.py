# app/schemas/epstb.py
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class EpstbBase(BaseModel):
    # TB004..TB043
    tb004: Optional[constr(max_length=4)] = None     # 訂單單別
    tb005: Optional[constr(max_length=11)] = None    # 訂單單號
    tb006: Optional[constr(max_length=4)] = None     # 訂單序號
    tb007: Optional[constr(max_length=20)] = None    # 品號
    tb008: Optional[constr(max_length=255)] = None   # 商品描述 (varchar)
    tb009: Optional[Decimal] = None                  # 出貨數量 (11,3)
    tb010: Optional[constr(max_length=1)] = None     # 類型(1:贈品量/2:備品量)
    tb011: Optional[Decimal] = None                  # 贈備品量 (11,3)
    tb012: Optional[Decimal] = None                  # 單價-1 (13,4)
    tb013: Optional[Decimal] = None                  # 金額-1 (13,2)
    tb014: Optional[Decimal] = None                  # 單價-2 (13,4)
    tb015: Optional[Decimal] = None                  # 金額-2 (13,2)
    tb016: Optional[Decimal] = None                  # 單價-3 (13,4)
    tb017: Optional[Decimal] = None                  # 金額-3 (13,2)
    tb018: Optional[constr(max_length=10)] = None    # 出貨倉庫
    tb019: Optional[constr(max_length=20)] = None    # 批號
    tb020: Optional[constr(max_length=255)] = None   # 備注 (varchar)
    tb021: Optional[constr(max_length=4)] = None     # 銷貨單別
    tb022: Optional[constr(max_length=11)] = None    # 銷貨單號
    tb023: Optional[constr(max_length=4)] = None     # 銷貨序號
    tb024: Optional[constr(max_length=1)] = None     # 更新碼 (Y/N)
    tb025: Optional[constr(max_length=1)] = None     # 審核碼 (Y/N)
    tb026: Optional[constr(max_length=60)] = None    # 品名 (varchar 60)
    tb027: Optional[constr(max_length=60)] = None    # 規格 (varchar 60)
    tb028: Optional[constr(max_length=4)] = None     # 單位
    tb029: Optional[Decimal] = None                  # 預計出貨數量 (11,3)
    tb030: Optional[Decimal] = None                  # 預計贈備品量 (11,3)
    tb031: Optional[constr(max_length=20)] = None    # 客戶品號
    tb032: Optional[Decimal] = None                  # 折扣率 (5,4)
    tb033: Optional[constr(max_length=3)] = None     # 包裝方式
    tb034: Optional[Decimal] = None                  # 毛重(Kg) (8,3)
    tb035: Optional[Decimal] = None                  # 材積(CUFT) (8,3)
    tb036: Optional[Decimal] = None                  # 預計出貨包裝數量 (11,3)
    tb037: Optional[Decimal] = None                  # 預計贈備品包裝量 (11,3)
    tb038: Optional[Decimal] = None                  # 出貨包裝數量 (11,3)
    tb039: Optional[Decimal] = None                  # 贈備品包裝量 (11,3)
    tb040: Optional[constr(max_length=4)] = None     # 包裝單位
    tb041: Optional[constr(max_length=10)] = None    # 庫位
    tb042: Optional[constr(max_length=1)] = None     # 庫位處理狀態(N/C/D)
    tb043: Optional[constr(max_length=1)] = None     # 掃碼生成標志(Y/N)

    # TB044..UDF56
    tb044: Optional[constr(max_length=30)] = None    # 預留字段 (varchar 30)
    tb045: Optional[Decimal] = None                  # 長 (13,2)
    tb046: Optional[Decimal] = None                  # 寬 (13,2)
    tb047: Optional[Decimal] = None                  # 高 (13,2)

    udf01: Optional[constr(max_length=60)] = None    # 客戶編號
    udf02: Optional[constr(max_length=60)] = None    # 預計貨櫃
    udf03: Optional[constr(max_length=60)] = None    # 燈種類型
    udf04: Optional[constr(max_length=60)] = None    # 產品用料成分
    udf05: Optional[constr(max_length=60)] = None    # 出貨工廠代號
    udf06: Optional[constr(max_length=60)] = None    # 自定義6

    udf51: Optional[Decimal] = None                  # 淨重 (15,6)
    udf52: Optional[Decimal] = None                  # 材積(CBM) (15,6)
    udf53: Optional[Decimal] = None                  # 單箱包裝數量(支/箱) (15,6)
    udf54: Optional[Decimal] = None                  # (15,6)
    udf55: Optional[Decimal] = None                  # (15,6)
    udf56: Optional[Decimal] = None                  # (15,6)

class EpstbCreate(InBase, EpstbBase):
    tb001: constr(max_length=4)     # 通知單別 (PK1)
    tb002: constr(max_length=11)    # 通知單號 (PK2)
    tb003: constr(max_length=4)     # 通知序號 (PK3)

class EpstbUpdate(InBase, EpstbBase):
    pass

class EpstbOut(OutBase, EpstbBase):
    tb001: str
    tb002: str
    tb003: str
    model_config = ConfigDict(from_attributes=True)
