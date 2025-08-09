# app/api/v1/__init__.py
from fastapi import APIRouter
from app.api.v1 import coptc, coptd, coptg, copth, epscd, epscm, epsta, epstb  # giữ sample nếu bạn đang dùng

api_router = APIRouter()
api_router.include_router(coptc.router)
api_router.include_router(coptd.router)
api_router.include_router(coptg.router)
api_router.include_router(copth.router)
api_router.include_router(epscd.router)
api_router.include_router(epscm.router)
api_router.include_router(epsta.router)
api_router.include_router(epstb.router)

