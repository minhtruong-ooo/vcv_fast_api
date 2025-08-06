from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.copth import CopthCreate, CopthUpdate, CopthOut
from app.services.copth_service import (
    get_copth, get_multi_copth, create_copth, update_copth, remove_copth
)

router = APIRouter(prefix="/copth", tags=["COPTH(銷貨單單身檔) - Sales Order Single Document"])

@router.get("/", response_model=List[CopthOut])
def list_copth(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    th001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search in th002/th004/th019"),
):
    items, _ = get_multi_copth(db, skip=skip, limit=limit, th001=th001, keyword=keyword)
    # đảm bảo serializer chạy để trim khoảng trắng
    return [CopthOut.model_validate(x) for x in items]

@router.get("/{th001}/{th002}/{th003}", response_model=CopthOut)
def get_one_copth(
    th001: str, th002: str, th003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_copth(db, th001, th002, th003)
    if not obj: raise HTTPException(status_code=404, detail="COPTH not found")
    return CopthOut.model_validate(obj)

@router.post("/", response_model=CopthOut, status_code=status.HTTP_201_CREATED)
def create_one_copth(
    data: CopthCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = create_copth(db, data)
    return CopthOut.model_validate(obj)

@router.put("/{th001}/{th002}/{th003}", response_model=CopthOut)
def update_one_copth(
    th001: str, th002: str, th003: str, data: CopthUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = update_copth(db, th001, th002, th003, data)
    return CopthOut.model_validate(obj)

@router.delete("/{th001}/{th002}/{th003}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_copth(
    th001: str, th002: str, th003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_copth(db, th001, th002, th003)
    return None
