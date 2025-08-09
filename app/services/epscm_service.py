from typing import List, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import HTTPException, status

from app.models.epscm import Epscm
from app.schemas.epscm import EpscmCreate, EpscmUpdate

def get_epscm(db: Session, cm001: str, cm002: str) -> Optional[Epscm]:
    return db.query(Epscm).filter(Epscm.cm001 == cm001, Epscm.cm002 == cm002).first()

def get_multi_epscm(
    db: Session,
    skip: int = 0,
    limit: int = 50,
    cm001: Optional[str] = None,
    keyword: Optional[str] = None,   # tìm theo số đơn / khách / số xuất
) -> Tuple[List[Epscm], int]:
    q = db.query(Epscm)
    if cm001:
        q = q.filter(Epscm.cm001 == cm001)
    if keyword:
        like = f"%{keyword}%"
        q = q.filter(or_(
            Epscm.cm002.ilike(like),  # 報關單單號
            Epscm.cm004.ilike(like),  # 客戶編號
            Epscm.cm010.ilike(like),  # 出貨單號
        ))
    total = q.count()
    items = q.order_by(Epscm.cm001, Epscm.cm002).offset(skip).limit(limit).all()
    return items, total

def create_epscm(db: Session, data: EpscmCreate) -> Epscm:
    if get_epscm(db, data.cm001, data.cm002):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="EPSCM already exists")
    obj = Epscm(**data.model_dump(exclude_unset=True))
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def update_epscm(db: Session, cm001: str, cm002: str, data: EpscmUpdate) -> Epscm:
    obj = get_epscm(db, cm001, cm002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSCM not found")
    payload = data.model_dump(exclude_unset=True)
    payload.pop("cm001", None); payload.pop("cm002", None)  # không đổi PK
    for k, v in payload.items(): setattr(obj, k, v)
    db.add(obj); db.commit(); db.refresh(obj); return obj

def remove_epscm(db: Session, cm001: str, cm002: str) -> None:
    obj = get_epscm(db, cm001, cm002)
    if not obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EPSCM not found")
    db.delete(obj); db.commit()

# (tuỳ chọn) alias nếu còn nơi khác dùng tên chung
get = get_epscm; get_multi = get_multi_epscm; create = create_epscm; update = update_epscm; remove = remove_epscm
