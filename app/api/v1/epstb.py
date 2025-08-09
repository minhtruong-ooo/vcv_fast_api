# app/api/v1/epstb.py
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.epstb import EpstbCreate, EpstbUpdate, EpstbOut
from app.services.epstb_service import (
    get_epstb, get_multi_epstb, create_epstb, update_epstb, remove_epstb
)

router = APIRouter(prefix="/epstb", tags=["EPSTB(出貨通知單單身檔) - Shipping Notification Single Document"])

@router.get("/", response_model=List[EpstbOut])
def list_epstb(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    tb001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search tb002/tb007/tb031/tb022"),
):
    items, _ = get_multi_epstb(db, skip=skip, limit=limit, tb001=tb001, keyword=keyword)
    # ép serialize để OutBase trim CHAR padding
    return [EpstbOut.model_validate(x) for x in items]

@router.get("/{tb001}/{tb002}/{tb003}", response_model=EpstbOut)
def get_one_epstb(
    tb001: str, tb002: str, tb003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_epstb(db, tb001, tb002, tb003)
    if not obj: raise HTTPException(status_code=404, detail="EPSTB not found")
    return EpstbOut.model_validate(obj)

@router.post("/", response_model=EpstbOut, status_code=status.HTTP_201_CREATED)
def create_one_epstb(
    data: EpstbCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = create_epstb(db, data)
    return EpstbOut.model_validate(obj)

@router.put("/{tb001}/{tb002}/{tb003}", response_model=EpstbOut)
def update_one_epstb(
    tb001: str, tb002: str, tb003: str, data: EpstbUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = update_epstb(db, tb001, tb002, tb003, data)
    return EpstbOut.model_validate(obj)

@router.delete("/{tb001}/{tb002}/{tb003}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_epstb(
    tb001: str, tb002: str, tb003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_epstb(db, tb001, tb002, tb003)
    return None
