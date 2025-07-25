# app/api/v1/sample.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.db.deps import get_db
from app.models.sample import Sample

router = APIRouter()

@router.get("/samples")
def read_samples(
    user=Depends(get_current_user), 
    db: Session = Depends(get_db)
):
    samples = db.query(Sample).all()
    return {
        "username": user['preferred_username'],
        "data": [{"id": s.id, "name": s.name} for s in samples]
    }