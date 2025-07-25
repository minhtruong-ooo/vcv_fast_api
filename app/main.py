from fastapi import FastAPI
from fastapi.security import OAuth2AuthorizationCodeBearer
from app.api.v1 import sample
from app.core.config import settings

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
)

app = FastAPI(
    title="Postgres + FastAPI + Keycloak JWT",
    version="1.0.0",
    swagger_ui_init_oauth={
        "clientId": settings.KEYCLOAK_CLIENT_ID,
        "usePkceWithAuthorizationCodeGrant": True,
    }
)

app.include_router(sample.router, prefix="/api/v1")