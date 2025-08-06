from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class CoptgBase(BaseModel):
    # TG003..TG043 (trừ PK để đặt ở Create/Out)
    tg003: Optional[constr(max_length=8)] = None     # 銷貨日期 (YMD)
    tg004: Optional[constr(max_length=10)] = None    # 客戶編號
    tg005: Optional[constr(max_length=6)] = None     # 部門
    tg006: Optional[constr(max_length=10)] = None    # 業務員
    tg007: Optional[constr(max_length=72)] = None    # 客戶全稱
    tg008: Optional[constr(max_length=72)] = None    # 送貨地址一
    tg009: Optional[constr(max_length=72)] = None    # 送貨地址二
    tg010: Optional[constr(max_length=6)] = None     # 出貨工廠
    tg011: Optional[constr(max_length=4)] = None     # 幣種
    tg012: Optional[Decimal] = None                  # 匯率 (10,7) 7.4->10.7
    tg013: Optional[Decimal] = None                  # 原幣銷貨金額 (13,2)
    tg014: Optional[constr(max_length=10)] = None    # 發票號碼
    tg015: Optional[constr(max_length=20)] = None    # 稅號
    tg016: Optional[constr(max_length=1)] = None     # 發票種類
    tg017: Optional[constr(max_length=1)] = None     # 稅種
    tg018: Optional[constr(max_length=72)] = None    # 發票地址一
    tg019: Optional[constr(max_length=72)] = None    # 發票地址二
    tg020: Optional[constr(max_length=255)] = None   # 備注
    tg021: Optional[constr(max_length=8)] = None     # 發票日期 (YMD)
    tg022: Optional[int] = None                      # 打印次數
    tg023: Optional[constr(max_length=1)] = None     # 審核碼
    tg024: Optional[constr(max_length=1)] = None     # 更新碼
    tg025: Optional[Decimal] = None                  # 原幣銷貨稅額 (13,2)
    tg026: Optional[constr(max_length=10)] = None    # 收款業務員
    tg027: Optional[constr(max_length=20)] = None    # 備注一
    tg028: Optional[constr(max_length=20)] = None    # 備注二
    tg029: Optional[constr(max_length=20)] = None    # 備注三
    tg030: Optional[constr(max_length=1)] = None     # 發票作廢
    tg031: Optional[constr(max_length=1)] = None     # 煙酒注記
    tg032: Optional[int] = None                      # 件數
    tg033: Optional[Decimal] = None                  # 總數量 (11,3)
    tg034: Optional[constr(max_length=1)] = None     # 現銷
    tg035: Optional[constr(max_length=10)] = None    # 員工編號
    tg036: Optional[constr(max_length=1)] = None     # 生成分錄(收入)
    tg037: Optional[constr(max_length=1)] = None     # 生成分錄(成本)
    tg038: Optional[constr(max_length=6)] = None     # 申報年月 (YM)
    tg039: Optional[constr(max_length=20)] = None    # L/C_NO
    tg040: Optional[constr(max_length=20)] = None    # INVOICE_NO
    tg041: Optional[int] = None                      # 發票打印次數
    tg042: Optional[constr(max_length=8)] = None     # 單據日期 (YMD)
    tg043: Optional[constr(max_length=10)] = None    # 審核者

    # TG044..TG073
    tg044: Optional[Decimal] = None                  # 稅率 (5,4)
    tg045: Optional[Decimal] = None                  # 本幣銷貨金額 (13,2)
    tg046: Optional[Decimal] = None                  # 本幣銷貨稅額 (13,2)
    tg047: Optional[constr(max_length=6)] = None     # 付款條件編號
    tg048: Optional[constr(max_length=4)] = None     # 訂單單別
    tg049: Optional[constr(max_length=11)] = None    # 訂單單號
    tg050: Optional[constr(max_length=4)] = None     # 預收待抵單別
    tg051: Optional[constr(max_length=11)] = None    # 預收待抵單號
    tg052: Optional[Decimal] = None                  # 沖抵金額 (13,2)
    tg053: Optional[Decimal] = None                  # 沖抵稅額 (13,2)
    tg054: Optional[Decimal] = None                  # 總包裝數量 (11,3)
    tg055: Optional[constr(max_length=1)] = None     # 簽核狀態碼
    tg056: Optional[constr(max_length=1)] = None     # 更換發票碼 (Y/N)
    tg057: Optional[constr(max_length=4)] = None     # 新銷貨單別
    tg058: Optional[constr(max_length=11)] = None    # 新銷貨單號
    tg059: Optional[constr(max_length=1)] = None     # 拋轉狀態
    tg060: Optional[constr(max_length=2)] = None     # 流程編號
    tg061: Optional[constr(max_length=1)] = None     # 隨貨附發票 (Y/N)
    tg064: Optional[constr(max_length=10)] = None    # 開票人
    tg065: Optional[constr(max_length=12)] = None    # 發票代碼
    tg066: Optional[constr(max_length=15)] = None    # 海關手冊
    tg067: Optional[int] = None                      # 傳送次數
    tg068: Optional[constr(max_length=1)] = None     # 發送消息狀態 (Y/N)
    tg069: Optional[constr(max_length=8)] = None     # 預留字段
    tg070: Optional[constr(max_length=30)] = None    # 預留字段
    tg071: Optional[Decimal] = None                  # 預留字段 (13,2)
    tg072: Optional[Decimal] = None                  # 預留字段 (13,2)
    tg073: Optional[Decimal] = None                  # 預留字段 (13,2)

    # UDF01..UDF06, UDF51..UDF56, UDF57..UDF59
    udf01: Optional[constr(max_length=500)] = None   # 香港Invoice備注
    udf02: Optional[constr(max_length=60)] = None
    udf03: Optional[constr(max_length=60)] = None
    udf04: Optional[constr(max_length=60)] = None
    udf05: Optional[constr(max_length=60)] = None
    udf06: Optional[constr(max_length=60)] = None
    udf51: Optional[Decimal] = None                  # PLUS (15,6)
    udf52: Optional[Decimal] = None                  # LESS (15,6)
    udf53: Optional[Decimal] = None                  # (15,6)
    udf54: Optional[Decimal] = None                  # (15,6)
    udf55: Optional[Decimal] = None                  # (15,6)
    udf56: Optional[Decimal] = None                  # (15,6)
    udf57: Optional[datetime] = None                 # 貨櫃到廠時間
    udf58: Optional[datetime] = None                 # 貨櫃離廠時間
    udf59: Optional[datetime] = None                 # 貨櫃入閘時間

class CoptgCreate(InBase, CoptgBase):
    tg001: constr(max_length=4)      # 單別
    tg002: constr(max_length=11)     # 單號

class CoptgUpdate(InBase, CoptgBase):
    pass

class CoptgOut(OutBase, CoptgBase):
    tg001: str
    tg002: str
    model_config = ConfigDict(from_attributes=True)
