# app/services/epstb_service.py
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.epstb import Epstb
from app.schemas.epstb import EpstbCreate, EpstbUpdate

def get_epstb(db: Session, tb001: str, tb002: str, tb003: str) -> Optional[Epstb]:
    return (
        db.query(Epstb)
          .filter(Epstb.tb001 == tb001, Epstb.tb002 == tb002, Epstb.tb003 == tb003)
          .first()
    )

def get_multi_epstb(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    tb001: Optional[str] = None,           # filter đơn loại
    keyword: Optional[str] = None,         # tìm theo số đơn/mã hàng/khách/SO
) -> Tuple[List[Epstb], int]:
    q = db.query(Epstb)
    if tb001:
        q = q.filter(Epstb.tb001 == tb001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter(or_(
            Epstb.tb002.ilike(like),  # 通知單號
            Epstb.tb007.ilike(like),  # 品號
            Epstb.tb031.ilike(like),  # 客戶品號
            Epstb.tb022.ilike(like),  # 銷貨單號
        ))
    total = q.count()
    items = q.order_by(Epstb.tb001, Epstb.tb002, Epstb.tb003).offset(skip).limit(limit).all()
    return items, total

def create_epstb(db: Session, data: EpstbCreate) -> Epstb:
    if get_epstb(db, data.tb001, data.tb002, data.tb003):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="EPSTB already exists")
    obj = Epstb(**data.model_dump(exclude_unset=True))
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def update_epstb(db: Session, tb001: str, tb002: str, tb003: str, data: EpstbUpdate) -> Epstb:
    obj = get_epstb(db, tb001, tb002, tb003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSTB not found")
    payload = data.model_dump(exclude_unset=True)
    for k in ("tb001", "tb002", "tb003"):
        payload.pop(k, None)  # không đổi PK
    for k, v in payload.items():
        setattr(obj, k, v)
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def remove_epstb(db: Session, tb001: str, tb002: str, tb003: str) -> None:
    obj = get_epstb(db, tb001, tb002, tb003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSTB not found")
    db.delete(obj); db.commit()

# alias (tuỳ chọn) nếu còn nơi khác dùng tên chung
get = get_epstb; get_multi = get_multi_epstb; create = create_epstb; update = update_epstb; remove = remove_epstb
