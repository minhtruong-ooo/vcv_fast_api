from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.coptg import Coptg
from app.schemas.coptg import CoptgCreate, CoptgUpdate

def get_coptg(db: Session, tg001: str, tg002: str) -> Optional[Coptg]:
    return db.query(Coptg).filter(Coptg.tg001 == tg001, Coptg.tg002 == tg002).first()

def get_multi_coptg(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    tg001: Optional[str] = None,
    keyword: Optional[str] = None,   # tìm trong số đơn / invoice
) -> Tuple[List[Coptg], int]:
    q = db.query(Coptg)
    if tg001:
        q = q.filter(Coptg.tg001 == tg001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter(or_(Coptg.tg002.ilike(like), Coptg.tg014.ilike(like), Coptg.tg040.ilike(like)))
    total = q.count()
    items = q.order_by(Coptg.tg001, Coptg.tg002).offset(skip).limit(limit).all()
    return items, total

def create_coptg(db: Session, data: CoptgCreate) -> Coptg:
    if get_coptg(db, data.tg001, data.tg002):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="COPTG already exists")
    obj = Coptg(**data.model_dump(exclude_unset=True))
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def update_coptg(db: Session, tg001: str, tg002: str, data: CoptgUpdate) -> Coptg:
    obj = get_coptg(db, tg001, tg002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTG not found")
    payload = data.model_dump(exclude_unset=True)
    payload.pop("tg001", None); payload.pop("tg002", None)  # không đổi PK
    for k, v in payload.items(): setattr(obj, k, v)
    db.add(obj); db.commit(); db.refresh(obj); return obj

def remove_coptg(db: Session, tg001: str, tg002: str) -> None:
    obj = get_coptg(db, tg001, tg002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTG not found")
    db.delete(obj); db.commit()

# (tuỳ chọn) alias nếu bạn còn router cũ dùng tên chung
get = get_coptg; get_multi = get_multi_coptg; create = create_coptg; update = update_coptg; remove = remove_coptg
