# app/api/v1/epsta.py
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.epsta import EpstaCreate, EpstaUpdate, EpstaOut
from app.services.epsta_service import (
    get_epsta, get_multi_epsta, create_epsta, update_epsta, remove_epsta
)

router = APIRouter(prefix="/epsta", tags=["EPSTA(出貨通知單單頭檔) - Shipment Notification Document Header"])

@router.get("/", response_model=List[EpstaOut])
def list_epsta(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    ta001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search ta002/ta042/ta049/ta040"),
):
    items, _ = get_multi_epsta(db, skip=skip, limit=limit, ta001=ta001, keyword=keyword)
    return [EpstaOut.model_validate(x) for x in items]  # ép serialize để trim CHAR

@router.get("/{ta001}/{ta002}", response_model=EpstaOut)
def get_one_epsta(
    ta001: str, ta002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_epsta(db, ta001, ta002)
    if not obj: raise HTTPException(status_code=404, detail="EPSTA not found")
    return EpstaOut.model_validate(obj)

@router.post("/", response_model=EpstaOut, status_code=status.HTTP_201_CREATED)
def create_one_epsta(
    data: EpstaCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = create_epsta(db, data)
    return EpstaOut.model_validate(obj)

@router.put("/{ta001}/{ta002}", response_model=EpstaOut)
def update_one_epsta(
    ta001: str, ta002: str, data: EpstaUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = update_epsta(db, ta001, ta002, data)
    return EpstaOut.model_validate(obj)

@router.delete("/{ta001}/{ta002}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_epsta(
    ta001: str, ta002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_epsta(db, ta001, ta002)
    return None
