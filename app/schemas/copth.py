from typing import Optional
from decimal import Decimal
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class CopthBase(BaseModel):
    # TH004..TH062
    th004: Optional[constr(max_length=20)] = None   # 品號
    th005: Optional[constr(max_length=60)] = None   # 品名 (varchar)
    th006: Optional[constr(max_length=60)] = None   # 規格 (varchar)
    th007: Optional[constr(max_length=10)] = None   # 倉庫
    th008: Optional[Decimal] = None                 # 數量 (11,3)
    th009: Optional[constr(max_length=4)] = None    # 單位
    th010: Optional[Decimal] = None                 # 庫存數量 (11,3)
    th011: Optional[constr(max_length=4)] = None    # 小單位
    th012: Optional[Decimal] = None                 # 單價 (15,6)
    th013: Optional[Decimal] = None                 # 金額 (13,2)
    th014: Optional[constr(max_length=4)] = None    # 訂單單別
    th015: Optional[constr(max_length=11)] = None   # 訂單單號
    th016: Optional[constr(max_length=4)] = None    # 訂單序號
    th017: Optional[constr(max_length=20)] = None   # 批號
    th018: Optional[constr(max_length=255)] = None  # 備注 (varchar)
    th019: Optional[constr(max_length=50)] = None   # 客戶品號
    th020: Optional[constr(max_length=1)] = None    # 審核碼 (Y/N/V)
    th021: Optional[constr(max_length=1)] = None    # 更新碼 (Y/N)
    th022: Optional[constr(max_length=8)] = None    # 保留字段/原銷貨日期
    th023: Optional[constr(max_length=10)] = None   # 保留字段/原客戶編號
    th024: Optional[Decimal] = None                 # 贈/備品量 (11,3)
    th025: Optional[Decimal] = None                 # 折扣率 (5,4)
    th026: Optional[constr(max_length=1)] = None    # 結賬碼 (Y/N)
    th027: Optional[constr(max_length=4)] = None    # 結賬單別
    th028: Optional[constr(max_length=11)] = None   # 結賬單號
    th029: Optional[constr(max_length=4)] = None    # 結賬序號
    th030: Optional[constr(max_length=20)] = None   # 項目編號
    th031: Optional[constr(max_length=1)] = None    # 類型(1:贈品/2:備品)
    th032: Optional[constr(max_length=4)] = None    # 借出單別
    th033: Optional[constr(max_length=11)] = None   # 借出單號
    th034: Optional[constr(max_length=4)] = None    # 借出序號
    th035: Optional[Decimal] = None                 # 原幣稅前金額 (13,2)
    th036: Optional[Decimal] = None                 # 原幣稅額 (13,2)
    th037: Optional[Decimal] = None                 # 本幣稅前金額 (13,2)
    th038: Optional[Decimal] = None                 # 本幣稅額 (13,2)
    th039: Optional[Decimal] = None                 # 包裝數量 (11,3)
    th040: Optional[Decimal] = None                 # 贈/備品包裝量 (11,3)
    th041: Optional[constr(max_length=4)] = None    # 包裝單位
    th042: Optional[Decimal] = None                 # 已結賬數量 (11,3)
    th043: Optional[Decimal] = None                 # 件裝 (11,3)
    th044: Optional[Decimal] = None                 # 件數 (11,3)
    th045: Optional[constr(max_length=4)] = None    # 出貨通知單別
    th046: Optional[constr(max_length=11)] = None   # 出貨通知單號
    th047: Optional[constr(max_length=4)] = None    # 出貨通知序號
    th048: Optional[Decimal] = None                 # 預留-稅率(%) (5,4)
    th049: Optional[Decimal] = None                 # 批發價 (15,6)
    th050: Optional[Decimal] = None                 # 零售價 (15,6)
    th051: Optional[constr(max_length=8)] = None    # 生產/有效日期 (YMD)
    th052: Optional[constr(max_length=8)] = None    # 有效日期 (YMD)
    th053: Optional[constr(max_length=8)] = None    # 復檢日期 (YMD)
    th054: Optional[constr(max_length=10)] = None   # 原始客戶
    th055: Optional[constr(max_length=80)] = None   # 批號說明 (varchar)
    th056: Optional[constr(max_length=10)] = None   # 庫位
    th057: Optional[constr(max_length=1)] = None    # 預留字段
    th058: Optional[constr(max_length=8)] = None    # 預留字段
    th059: Optional[constr(max_length=30)] = None   # 預留字段 (varchar)
    th060: Optional[Decimal] = None                 # 預留字段 (13,2)
    th061: Optional[Decimal] = None                 # 預留字段 (13,2)
    th062: Optional[Decimal] = None                 # 預留字段 (13,2)

    # UDF01..UDF06 (varchar 60), UDF51..UDF56 (numeric 15,6)
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

    # 系統欄位
    company: Optional[constr(max_length=10)] = None
    creator: Optional[constr(max_length=10)] = None
    usr_group: Optional[constr(max_length=10)] = None
    create_date: Optional[constr(max_length=17)] = None
    modifier: Optional[constr(max_length=10)] = None
    modi_date: Optional[constr(max_length=17)] = None
    flag: Optional[Decimal] = None                  # (5,3)

class CopthCreate(InBase, CopthBase):
    th001: constr(max_length=4)     # 單別
    th002: constr(max_length=11)    # 單號
    th003: constr(max_length=4)     # 序號

class CopthUpdate(InBase, CopthBase):
    pass

class CopthOut(OutBase, CopthBase):
    th001: str
    th002: str
    th003: str
    model_config = ConfigDict(from_attributes=True)
