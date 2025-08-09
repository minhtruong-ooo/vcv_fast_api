from typing import Optional
from decimal import Decimal
from datetime import datetime
from pydantic import BaseModel, constr, ConfigDict
from app.schemas.common import InBase, OutBase

class EpscmBase(BaseModel):
    # CM003..CM012 (PK đặt ở Create/Out)
    cm003: Optional[constr(max_length=8)] = None     # 單據日期 (char 8)
    cm004: Optional[constr(max_length=10)] = None    # 客戶編號 (char 10)
    cm005: Optional[constr(max_length=30)] = None    # 聯系人 (char 30)
    cm006: Optional[constr(max_length=10)] = None    # 審核碼 (char 10)
    cm007: Optional[constr(max_length=10)] = None    # 審核日期 (char 10)
    cm008: Optional[constr(max_length=10)] = None    # 審核人 (char 10)
    cm009: Optional[constr(max_length=10)] = None    # 出貨單別 (char 10)
    cm010: Optional[constr(max_length=15)] = None    # 出貨單號 (char 15)
    cm011: Optional[constr(max_length=8)] = None     # 出貨單生成時間 (varchar 8)
    cm012: Optional[constr(max_length=200)] = None   # 備注 (varchar 200)

    # 同步欄位
    syncdate: Optional[datetime] = None              # SyncDate (datetime)
    # Tài liệu ghi numeric 9 / N18…; thường là numeric(18,0) → map int cho API
    syncflag: Optional[int] = None                   # SyncFlag

class EpscmCreate(InBase, EpscmBase):
    cm001: constr(max_length=4)      # 報關單別 (char 4)
    cm002: constr(max_length=11)     # 報關單單號 (char 11)

class EpscmUpdate(InBase, EpscmBase):
    pass

class EpscmOut(OutBase, EpscmBase):
    cm001: str
    cm002: str
    model_config = ConfigDict(from_attributes=True)
