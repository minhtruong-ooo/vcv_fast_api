# app/api/v1/__init__.py
from fastapi import APIRouter
from app.api.v1 import coptc, coptd, coptg, copth  # giữ sample nếu bạn đang dùng

api_router = APIRouter()
api_router.include_router(coptc.router)
api_router.include_router(coptd.router)
api_router.include_router(coptg.router)
api_router.include_router(copth.router)