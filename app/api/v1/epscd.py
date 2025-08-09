# app/api/v1/epscd.py
from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status, HTTPException
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.security import get_current_user
from app.schemas.epscd import EpscdCreate, EpscdUpdate, EpscdOut
from app.services.epscd_service import (
    get_epscd, get_multi_epscd, create_epscd, update_epscd, remove_epscd
)

router = APIRouter(prefix="/epscd", tags=["EPSCD(報關單單身) - Customs Declaration Single Document"])

@router.get("/", response_model=List[EpscdOut])
def list_epscd(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=200),
    cd001: Optional[str] = Query(None, max_length=4),
    keyword: Optional[str] = Query(None, description="Search in cd002/cd005/cd007/cd027/cd040/cd025"),
):
    items, _ = get_multi_epscd(db, skip=skip, limit=limit, cd001=cd001, keyword=keyword)
    # ép serialize qua Pydantic để trim CHAR padding
    return [EpscdOut.model_validate(x) for x in items]

@router.get("/{cd001}/{cd002}/{cd003}", response_model=EpscdOut)
def get_one_epscd(
    cd001: str, cd002: str, cd003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = get_epscd(db, cd001, cd002, cd003)
    if not obj: raise HTTPException(status_code=404, detail="EPSCD not found")
    return EpscdOut.model_validate(obj)

@router.post("/", response_model=EpscdOut, status_code=status.HTTP_201_CREATED)
def create_one_epscd(
    data: EpscdCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = create_epscd(db, data)
    return EpscdOut.model_validate(obj)

@router.put("/{cd001}/{cd002}/{cd003}", response_model=EpscdOut)
def update_one_epscd(
    cd001: str, cd002: str, cd003: str, data: EpscdUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    obj = update_epscd(db, cd001, cd002, cd003, data)
    return EpscdOut.model_validate(obj)

@router.delete("/{cd001}/{cd002}/{cd003}", status_code=status.HTTP_204_NO_CONTENT)
def delete_one_epscd(
    cd001: str, cd002: str, cd003: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    remove_epscd(db, cd001, cd002, cd003)
    return None
