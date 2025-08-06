# app/services/coptd_service.py
from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.coptd import Coptd
from app.schemas.coptd import CoptdCreate, CoptdUpdate


def get_coptd(db: Session, td001: str, td002: str, td003: str) -> Optional[Coptd]:
    return (
        db.query(Coptd)
          .filter(Coptd.td001 == td001, Coptd.td002 == td002, Coptd.td003 == td003)
          .first()
    )


def get_multi_coptd(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    td001: Optional[str] = None,
    keyword: Optional[str] = None,
) -> Tuple[List[Coptd], int]:
    q = db.query(Coptd)
    if td001:
        q = q.filter(Coptd.td001 == td001)
    if keyword:
        like = f"%{keyword}%"
        # Tìm trong số đơn và customer part (đổi cột theo nhu cầu của bạn)
        q = q.filter(or_(Coptd.td002.ilike(like), Coptd.td014.ilike(like)))

    total = q.count()
    items = (
        q.order_by(Coptd.td001, Coptd.td002, Coptd.td003)
         .offset(skip)
         .limit(limit)
         .all()
    )
    return items, total


def create_coptd(db: Session, data: CoptdCreate) -> Coptd:
    if get_coptd(db, data.td001, data.td002, data.td003):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="COPTD already exists")
    obj = Coptd(**data.model_dump(exclude_unset=True))
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def update_coptd(db: Session, td001: str, td002: str, td003: str, data: CoptdUpdate) -> Coptd:
    obj = get_coptd(db, td001, td002, td003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTD not found")

    payload = data.model_dump(exclude_unset=True)
    # Không cho phép đổi PK
    for k in ("td001", "td002", "td003"):
        payload.pop(k, None)

    for k, v in payload.items():
        setattr(obj, k, v)

    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


def remove_coptd(db: Session, td001: str, td002: str, td003: str) -> None:
    obj = get_coptd(db, td001, td002, td003)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="COPTD not found")
    db.delete(obj)
    db.commit()


# (Tuỳ chọn) Alias để tương thích ngược nếu nơi khác còn gọi tên cũ
get = get_coptd
get_multi = get_multi_coptd
create = create_coptd
update = update_coptd
remove = remove_coptd
