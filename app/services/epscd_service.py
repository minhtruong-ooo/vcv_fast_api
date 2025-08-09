# app/services/epscd_service.py
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.epscd import Epscd
from app.schemas.epscd import EpscdCreate, EpscdUpdate

def get_epscd(db: Session, cd001: str, cd002: str, cd003: str) -> Optional[Epscd]:
    return (
        db.query(Epscd)
          .filter(Epscd.cd001 == cd001, Epscd.cd002 == cd002, Epscd.cd003 == cd003)
          .first()
    )

def get_multi_epscd(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    cd001: Optional[str] = None,
    keyword: Optional[str] = None,   # tìm theo số đơn / mã hàng / SKU / khách
) -> Tuple[List[Epscd], int]:
    q = db.query(Epscd)
    if cd001:
        q = q.filter(Epscd.cd001 == cd001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter(or_(
            Epscd.cd002.ilike(like),  # 報關單號
            Epscd.cd005.ilike(like),  # 訂單單號
            Epscd.cd007.ilike(like),  # 品號
            Epscd.cd027.ilike(like),  # 客號
            Epscd.cd040.ilike(like),  # SKU
            Epscd.cd025.ilike(like),  # 客戶
        ))
    total = q.count()
    items = q.order_by(Epscd.cd001, Epscd.cd002, Epscd.cd003).offset(skip).limit(limit).all()
    return items, total

def create_epscd(db: Session, data: EpscdCreate) -> Epscd:
    if get_epscd(db, data.cd001, data.cd002, data.cd003):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="EPSCD already exists")
    obj = Epscd(**data.model_dump(exclude_unset=True))
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def update_epscd(db: Session, cd001: str, cd002: str, cd003: str, data: EpscdUpdate) -> Epscd:
    obj = get_epscd(db, cd001, cd002, cd003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSCD not found")
    payload = data.model_dump(exclude_unset=True)
    for k in ("cd001", "cd002", "cd003"): payload.pop(k, None)  # không đổi PK
    for k, v in payload.items(): setattr(obj, k, v)
    db.add(obj); db.commit(); db.refresh(obj); return obj

def remove_epscd(db: Session, cd001: str, cd002: str, cd003: str) -> None:
    obj = get_epscd(db, cd001, cd002, cd003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSCD not found")
    db.delete(obj); db.commit()

# (optional) alias nếu bạn còn router cũ dùng tên chung
get = get_epscd; get_multi = get_multi_epscd; create = create_epscd; update = update_epscd; remove = remove_epscd
