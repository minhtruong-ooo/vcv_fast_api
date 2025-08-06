from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.copth import Copth
from app.schemas.copth import CopthCreate, CopthUpdate

def get_copth(db: Session, th001: str, th002: str, th003: str) -> Optional[Copth]:
    return (
        db.query(Copth)
          .filter(Copth.th001 == th001, Copth.th002 == th002, Copth.th003 == th003)
          .first()
    )

def get_multi_copth(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    th001: Optional[str] = None,         # lọc theo 單別
    keyword: Optional[str] = None,       # tìm theo 單號/品號/客戶品號
) -> Tuple[List[Copth], int]:
    q = db.query(Copth)
    if th001:
        q = q.filter(Copth.th001 == th001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter(or_(Copth.th002.ilike(like), Copth.th004.ilike(like), Copth.th019.ilike(like)))
    total = q.count()
    items = q.order_by(Copth.th001, Copth.th002, Copth.th003).offset(skip).limit(limit).all()
    return items, total

def create_copth(db: Session, data: CopthCreate) -> Copth:
    if get_copth(db, data.th001, data.th002, data.th003):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="COPTH already exists")
    obj = Copth(**data.model_dump(exclude_unset=True))
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def update_copth(db: Session, th001: str, th002: str, th003: str, data: CopthUpdate) -> Copth:
    obj = get_copth(db, th001, th002, th003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTH not found")
    payload = data.model_dump(exclude_unset=True)
    for k in ("th001", "th002", "th003"):
        payload.pop(k, None)  # không đổi PK
    for k, v in payload.items():
        setattr(obj, k, v)
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def remove_copth(db: Session, th001: str, th002: str, th003: str) -> None:
    obj = get_copth(db, th001, th002, th003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTH not found")
    db.delete(obj); db.commit()

# (tuỳ chọn) alias cho tương thích chỗ khác nếu còn dùng tên chung
get = get_copth; get_multi = get_multi_copth; create = create_copth; update = update_copth; remove = remove_copth
