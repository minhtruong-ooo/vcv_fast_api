# app/schemas/epsta.py
from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class EpstaBase(BaseModel):
    # TA003..TA085 (PK đặt ở Create/Out)
    ta003: Optional[constr(max_length=8)] = None      # 通知日期 (YMD)
    ta004: Optional[constr(max_length=10)] = None     # 客戶編號
    ta005: Optional[constr(max_length=30)] = None     # 聯系人
    ta006: Optional[constr(max_length=6)] = None      # 部門編號
    ta007: Optional[constr(max_length=10)] = None     # 業務人員
    ta008: Optional[constr(max_length=10)] = None     # 送貨客戶
    ta009: Optional[constr(max_length=72)] = None     # 送貨地址(一)
    ta010: Optional[constr(max_length=72)] = None     # 送貨地址(二)
    ta011: Optional[constr(max_length=72)] = None     # 文件送達地址(一)
    ta012: Optional[constr(max_length=72)] = None     # 文件送達地址(二)
    ta013: Optional[constr(max_length=10)] = None     # 發票客戶
    ta014: Optional[constr(max_length=72)] = None     # 發票地址(一)
    ta015: Optional[constr(max_length=72)] = None     # 發票地址(二)
    ta016: Optional[constr(max_length=8)] = None      # 發票日期 (YMD)
    ta017: Optional[constr(max_length=10)] = None     # 發票號碼
    ta018: Optional[constr(max_length=20)] = None     # 稅號
    ta019: Optional[constr(max_length=1)] = None      # 發票種類
    ta020: Optional[constr(max_length=1)] = None      # 稅種
    ta021: Optional[constr(max_length=20)] = None     # L/C_NO
    ta022: Optional[constr(max_length=4)] = None      # 交易幣種
    ta023: Optional[Decimal] = None                   # 匯率 (numeric 10,7)
    ta024: Optional[constr(max_length=16)] = None     # 價格說明
    ta025: Optional[constr(max_length=16)] = None     # 付款條件
    ta026: Optional[constr(max_length=4)] = None      # 銷貨單別
    ta027: Optional[constr(max_length=11)] = None     # 銷貨單號
    ta028: Optional[constr(max_length=4)] = None      # 嘜頭
    ta029: Optional[Decimal] = None                   # 銷貨金額 (13,2)
    ta030: Optional[Decimal] = None                   # 包裝總數 (11,3)
    ta031: Optional[constr(max_length=1)] = None      # 運輸方式
    ta032: Optional[constr(max_length=1)] = None      # 更新碼 (Y/N)
    ta033: Optional[constr(max_length=1)] = None      # PACKING審核碼
    ta034: Optional[constr(max_length=1)] = None      # 審核碼 (Y/N)
    ta035: Optional[constr(max_length=20)] = None     # 輸出許可証號
    ta036: Optional[constr(max_length=20)] = None     # 大提單單號
    ta037: Optional[constr(max_length=20)] = None     # 小提單單號
    ta038: Optional[constr(max_length=10)] = None     # NOTIFY
    ta039: Optional[constr(max_length=8)] = None      # ETA (YMD)
    ta040: Optional[constr(max_length=8)] = None      # ETD (YMD)
    ta041: Optional[constr(max_length=6)] = None      # 出貨工廠
    ta042: Optional[constr(max_length=20)] = None     # INVOICE_NO
    ta043: Optional[constr(max_length=10)] = None     # 驗貨公司
    ta044: Optional[constr(max_length=10)] = None     # 報關行
    ta045: Optional[constr(max_length=10)] = None     # 運輸公司
    ta046: Optional[constr(max_length=20)] = None     # 貨櫃號碼
    ta047: Optional[Decimal] = None                   # 貨櫃體積 (≈3,1)
    ta048: Optional[constr(max_length=20)] = None     # 貨櫃場
    ta049: Optional[constr(max_length=30)] = None     # 船名
    ta050: Optional[constr(max_length=20)] = None     # 船次
    ta051: Optional[constr(max_length=20)] = None     # 報單號碼
    ta052: Optional[constr(max_length=8)] = None      # 結關日 (YMD)
    ta053: Optional[constr(max_length=8)] = None      # 裝貨日 (YMD)
    ta054: Optional[constr(max_length=8)] = None      # 裝船日 (YMD)
    ta055: Optional[constr(max_length=20)] = None     # S/I_NO
    ta056: Optional[constr(max_length=20)] = None     # 起始港口
    ta057: Optional[constr(max_length=20)] = None     # 目的港口
    ta058: Optional[constr(max_length=20)] = None     # 目的地
    ta059: Optional[constr(max_length=20)] = None     # 海關封簽
    ta060: Optional[constr(max_length=20)] = None     # 提單內容
    ta061: Optional[constr(max_length=10)] = None     # 海運公司
    ta062: Optional[constr(max_length=10)] = None     # 空運公司
    ta063: Optional[constr(max_length=255)] = None    # 正嘜 (varchar)
    ta064: Optional[constr(max_length=255)] = None    # 側嘜 (varchar)
    ta065: Optional[constr(max_length=255)] = None    # PACKING備注 (varchar)
    ta066: Optional[constr(max_length=255)] = None    # INVOICE備注 (varchar)
    ta067: Optional[constr(max_length=20)] = None     # 貨盤單位
    ta068: Optional[Decimal] = None                   # 銷貨稅額 (13,2)
    ta069: Optional[int] = None                       # 打印次數 (int)
    ta070: Optional[constr(max_length=8)] = None      # 單據日期 (YMD)
    ta071: Optional[constr(max_length=10)] = None     # 審核者
    ta072: Optional[constr(max_length=8)] = None      # PACKING審核日期
    ta073: Optional[constr(max_length=10)] = None     # PACKING審核者
    ta074: Optional[constr(max_length=6)] = None      # 付款條件編號
    ta075: Optional[constr(max_length=1)] = None      # 簽核狀態碼
    ta076: Optional[constr(max_length=1)] = None      # PACKING簽核狀態碼
    ta077: Optional[constr(max_length=15)] = None     # 海關手冊
    ta078: Optional[int] = None                       # 傳送次數 (int, DEF:0)
    ta079: Optional[constr(max_length=2)] = None      # 流程編號
    ta080: Optional[constr(max_length=1)] = None      # 外廠合用貨櫃 (Y/N)
    ta081: Optional[constr(max_length=8)] = None      # 在途中狀態 (Y/N or YMD)
    ta082: Optional[constr(max_length=30)] = None     # 報關方式 (varchar)
    ta083: Optional[Decimal] = None                   # 庫位管理狀態 (13,2)
    ta084: Optional[Decimal] = None                   # 預留字段 (13,2)
    ta085: Optional[Decimal] = None                   # 預留字段 (13,2)

    # UDF & 時間
    udf01: Optional[constr(max_length=60)] = None     # 封條
    udf02: Optional[constr(max_length=60)] = None     # 貨櫃尺寸
    udf03: Optional[constr(max_length=60)] = None     # 拖車公司
    udf04: Optional[constr(max_length=60)] = None     # CS跟進人
    udf05: Optional[constr(max_length=60)] = None     # 船務跟進人
    udf06: Optional[constr(max_length=60)] = None
    udf51: Optional[Decimal] = None                   # 通知單審核日期 (15,6)
    udf52: Optional[Decimal] = None                   # 總材積(CBM) (15,6)
    udf53: Optional[Decimal] = None
    udf54: Optional[Decimal] = None
    udf55: Optional[Decimal] = None
    udf56: Optional[Decimal] = None
    udf57: Optional[datetime] = None                  # 到廠時間
    udf58: Optional[datetime] = None                  # 離廠時間
    udf59: Optional[datetime] = None                  # 入閘時間
    udf07: Optional[constr(max_length=20)] = None     # 起貨點

    # 系統欄位
    company: Optional[constr(max_length=10)] = None
    creator: Optional[constr(max_length=10)] = None
    usr_group: Optional[constr(max_length=10)] = None
    create_date: Optional[constr(max_length=17)] = None
    modifier: Optional[constr(max_length=10)] = None
    modi_date: Optional[constr(max_length=17)] = None
    flag: Optional[Decimal] = None                    # (5,3)

class EpstaCreate(InBase, EpstaBase):
    ta001: constr(max_length=4)    # 通知單別 (PK1)
    ta002: constr(max_length=11)   # 通知單號 (PK2)

class EpstaUpdate(InBase, EpstaBase):
    pass

class EpstaOut(OutBase, EpstaBase):
    ta001: str
    ta002: str
    model_config = ConfigDict(from_attributes=True)
