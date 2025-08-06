# app/services/coptc_service.py
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.coptc import Coptc
from app.schemas.coptc import CoptcCreate, CoptcUpdate

def get(db: Session, tc001: str, tc002: str) -> Optional[Coptc]:
    return (
        db.query(Coptc)
          .filter(Coptc.tc001 == tc001, Coptc.tc002 == tc002)
          .first()
    )

def list_(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    tc001: Optional[str] = None,
    keyword: Optional[str] = None,
) -> List[Coptc]:
    q = db.query(Coptc)
    if tc001:
        q = q.filter(Coptc.tc001 == tc001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter((Coptc.tc002.ilike(like)) | (Coptc.tc012.ilike(like)))
    return q.offset(skip).limit(limit).all()

def get_multi(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    tc001: Optional[str] = None,
    keyword: Optional[str] = None,
) -> Tuple[List[Coptc], int]:
    q = db.query(Coptc)
    if tc001:
        q = q.filter(Coptc.tc001 == tc001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter((Coptc.tc002.ilike(like)) | (Coptc.tc012.ilike(like)))

    total = q.count()  # đếm trước khi phân trang
    items = q.order_by(Coptc.tc001, Coptc.tc002).offset(skip).limit(limit).all()
    return items, total

def create(db: Session, data: CoptcCreate) -> Coptc:
    if get(db, data.tc001, data.tc002):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="COPTC already exists")
    obj = Coptc(**data.model_dump(exclude_unset=True))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, tc001: str, tc002: str, data: CoptcUpdate) -> Coptc:
    obj = get(db, tc001, tc002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTC not found")
    payload = data.model_dump(exclude_unset=True)
    payload.pop("tc001", None)
    payload.pop("tc002", None)
    for k, v in payload.items():
        setattr(obj, k, v)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def remove(db: Session, tc001: str, tc002: str) -> None:
    obj = get(db, tc001, tc002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTC not found")
    db.delete(obj)
    db.commit()
