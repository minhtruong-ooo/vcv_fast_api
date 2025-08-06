# app/api/v1/coptd.py
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.coptd import CoptdCreate, CoptdUpdate, CoptdOut
from app.services.coptd_service import (
    get_coptd,
    get_multi_coptd,
    create_coptd,
    update_coptd,
    remove_coptd,
)

router = APIRouter(prefix="/coptd", tags=["COPTD(客戶訂單單身信息檔) - Customer Order Personal Information File"])

@router.get("/", response_model=List[CoptdOut])
def list_coptd(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    td001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search in td002 or td014"),
):
    items, _ = get_multi_coptd(db, skip=skip, limit=limit, td001=td001, keyword=keyword)
    return items

@router.get("/{td001}/{td002}/{td003}", response_model=CoptdOut)
def get_one_coptd(
    td001: str,
    td002: str,
    td003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_coptd(db, td001, td002, td003)
    if not obj:
        raise HTTPException(status_code=404, detail="COPTD not found")
    return obj

@router.post("/", response_model=CoptdOut, status_code=status.HTTP_201_CREATED)
def create_one_coptd(
    data: CoptdCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return create_coptd(db, data)

@router.put("/{td001}/{td002}/{td003}", response_model=CoptdOut)
def update_one_coptd(
    td001: str,
    td002: str,
    td003: str,
    data: CoptdUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return update_coptd(db, td001, td002, td003, data)

@router.delete("/{td001}/{td002}/{td003}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_coptd(
    td001: str,
    td002: str,
    td003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_coptd(db, td001, td002, td003)
    return None
