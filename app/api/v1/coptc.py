# app/api/v1/coptc.py
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.coptc import CoptcCreate, CoptcUpdate, CoptcOut
from app.services.coptc_service import get, get_multi, create, update, remove

router = APIRouter(prefix="/coptc", tags=["COPTC(客戶訂單單頭信息檔) - Customer Order Header Information"])

@router.get("/", response_model=List[CoptcOut])
def list_coptc(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    tc001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search in tc002 or tc012"),
):
    items, _ = get_multi(db, skip=skip, limit=limit, tc001=tc001, keyword=keyword)
    return items

@router.get("/{tc001}/{tc002}", response_model=CoptcOut)
def get_coptc(
    tc001: str,
    tc002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get(db, tc001, tc002)
    if not obj:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="COPTC not found")
    return obj

@router.post("/", response_model=CoptcOut, status_code=status.HTTP_201_CREATED)
def create_coptc(
    data: CoptcCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return create(db, data)

@router.put("/{tc001}/{tc002}", response_model=CoptcOut)
def update_coptc(
    tc001: str,
    tc002: str,
    data: CoptcUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    return update(db, tc001, tc002, data)

@router.delete("/{tc001}/{tc002}", status_code=status.HTTP_204_NO_CONTENT)
def delete_coptc(
    tc001: str,
    tc002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove(db, tc001, tc002)
    return None
