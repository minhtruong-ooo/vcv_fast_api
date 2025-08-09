# app/services/epsta_service.py
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.epsta import Epsta
from app.schemas.epsta import EpstaCreate, EpstaUpdate

def get_epsta(db: Session, ta001: str, ta002: str) -> Optional[Epsta]:
    return db.query(Epsta).filter(Epsta.ta001 == ta001, Epsta.ta002 == ta002).first()

def get_multi_epsta(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    ta001: Optional[str] = None,
    keyword: Optional[str] = None,  # search: số chứng từ / invoice / tàu
) -> Tuple[List[Epsta], int]:
    q = db.query(Epsta)
    if ta001:
        q = q.filter(Epsta.ta001 == ta001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter(or_(
            Epsta.ta002.ilike(like),  # 通知單號
            Epsta.ta042.ilike(like),  # INVOICE_NO
            Epsta.ta049.ilike(like),  # 船名
            Epsta.ta040.ilike(like),  # ETD
        ))
    total = q.count()
    items = q.order_by(Epsta.ta001, Epsta.ta002).offset(skip).limit(limit).all()
    return items, total

def create_epsta(db: Session, data: EpstaCreate) -> Epsta:
    if get_epsta(db, data.ta001, data.ta002):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="EPSTA already exists")
    obj = Epsta(**data.model_dump(exclude_unset=True))
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def update_epsta(db: Session, ta001: str, ta002: str, data: EpstaUpdate) -> Epsta:
    obj = get_epsta(db, ta001, ta002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSTA not found")
    payload = data.model_dump(exclude_unset=True)
    payload.pop("ta001", None); payload.pop("ta002", None)  # không đổi PK
    for k, v in payload.items(): setattr(obj, k, v)
    db.add(obj); db.commit(); db.refresh(obj); return obj

def remove_epsta(db: Session, ta001: str, ta002: str) -> None:
    obj = get_epsta(db, ta001, ta002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSTA not found")
    db.delete(obj); db.commit()

# (alias tuỳ chọn nếu còn nơi khác dùng tên chung)
get = get_epsta; get_multi = get_multi_epsta; create = create_epsta; update = update_epsta; remove = remove_epsta
