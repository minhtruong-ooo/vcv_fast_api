from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.epscm import EpscmCreate, EpscmUpdate, EpscmOut
from app.services.epscm_service import (
    get_epscm, get_multi_epscm, create_epscm, update_epscm, remove_epscm
)

router = APIRouter(prefix="/epscm", tags=["EPSCM(報關資料單頭) - Customs Declaration Header"])

@router.get("/", response_model=List[EpscmOut])
def list_epscm(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    cm001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search in cm002/cm004/cm010"),
):
    items, _ = get_multi_epscm(db, skip=skip, limit=limit, cm001=cm001, keyword=keyword)
    # đảm bảo OutBase serializer chạy để trim CHAR padding
    return [EpscmOut.model_validate(x) for x in items]

@router.get("/{cm001}/{cm002}", response_model=EpscmOut)
def get_one_epscm(
    cm001: str, cm002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_epscm(db, cm001, cm002)
    if not obj: raise HTTPException(status_code=404, detail="EPSCM not found")
    return EpscmOut.model_validate(obj)

@router.post("/", response_model=EpscmOut, status_code=status.HTTP_201_CREATED)
def create_one_epscm(
    data: EpscmCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = create_epscm(db, data)
    return EpscmOut.model_validate(obj)

@router.put("/{cm001}/{cm002}", response_model=EpscmOut)
def update_one_epscm(
    cm001: str, cm002: str, data: EpscmUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = update_epscm(db, cm001, cm002, data)
    return EpscmOut.model_validate(obj)

@router.delete("/{cm001}/{cm002}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_epscm(
    cm001: str, cm002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_epscm(db, cm001, cm002)
    return None
