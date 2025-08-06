# # app/main.py

# from fastapi import FastAPI
# from fastapi.security import OAuth2AuthorizationCodeBearer
# from app.api.v1 import sample
# from app.core.config import settings

# oauth2_scheme = OAuth2AuthorizationCodeBearer(
#     authorizationUrl=f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/auth",
#     tokenUrl=f"{settings.KEYCLOAK_URL}/realms/{settings.KEYCLOAK_REALM}/protocol/openid-connect/token"
# )

# app = FastAPI(
#     title="Postgres + FastAPI + Keycloak JWT -> EPS Module",
#     version="1.0.0",
#     swagger_ui_init_oauth={
#         "clientId": settings.KEYCLOAK_CLIENT_ID,
#         "usePkceWithAuthorizationCodeGrant": True,
#     }
# )



from fastapi import FastAPI
from app.api.v1 import api_router
from app.core.config import settings

app = FastAPI(
    title="PostgresSQL + FastAPI + Keycloak JWT -> EPS Module",
    version="1.0.0",
    swagger_ui_init_oauth={
        "clientId": settings.KEYCLOAK_CLIENT_ID,
        "usePkceWithAuthorizationCodeGrant": True,
    },
)

app.include_router(api_router, prefix="/api/v1")
