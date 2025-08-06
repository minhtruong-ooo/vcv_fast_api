from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.coptg import CoptgCreate, CoptgUpdate, CoptgOut
from app.services.coptg_service import (
    get_coptg, get_multi_coptg, create_coptg, update_coptg, remove_coptg
)

router = APIRouter(prefix="/coptg", tags=["COPTG(銷貨單單頭檔) - Sales Order Header Document"])

@router.get("/", response_model=List[CoptgOut])
def list_coptg(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    tg001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search in tg002/tg014/tg040"),
):
    items, _ = get_multi_coptg(db, skip=skip, limit=limit, tg001=tg001, keyword=keyword)
    # đảm bảo OutBase serializer chạy (trim CHAR)
    return [CoptgOut.model_validate(x) for x in items]

@router.get("/{tg001}/{tg002}", response_model=CoptgOut)
def get_one_coptg(
    tg001: str, tg002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_coptg(db, tg001, tg002)
    if not obj: raise HTTPException(status_code=404, detail="COPTG not found")
    return CoptgOut.model_validate(obj)

@router.post("/", response_model=CoptgOut, status_code=status.HTTP_201_CREATED)
def create_one_coptg(
    data: CoptgCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = create_coptg(db, data)
    return CoptgOut.model_validate(obj)

@router.put("/{tg001}/{tg002}", response_model=CoptgOut)
def update_one_coptg(
    tg001: str, tg002: str, data: CoptgUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = update_coptg(db, tg001, tg002, data)
    return CoptgOut.model_validate(obj)

@router.delete("/{tg001}/{tg002}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_coptg(
    tg001: str, tg002: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_coptg(db, tg001, tg002)
    return None
