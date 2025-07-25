from fastapi import Depends, HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import jwt, JWTError
import requests

KEYCLOAK_URL = "http://192.168.28.38:8888"
REALM = "fastapi"
ALGORITHMS = ["RS256"]
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/token"
)

def get_jwk_key(token):
    # Lấy phần header để đọc 'kid'
    unverified_header = jwt.get_unverified_header(token)
    kid = unverified_header.get("kid")
    if not kid:
        raise HTTPException(status_code=401, detail="Token header missing 'kid'")
    
    jwks_url = f"{KEYCLOAK_URL}/realms/{REALM}/protocol/openid-connect/certs"
    jwks = requests.get(jwks_url).json()
    for key in jwks["keys"]:
        if key["kid"] == kid:
            return key
    raise HTTPException(status_code=401, detail="Public key not found in JWKS")

def decode_token(token: str):
    key = get_jwk_key(token)
    try:
        payload = jwt.decode(
            token,
            key,
            algorithms=ALGORITHMS,
            options={"verify_aud": False}  # Bỏ kiểm tra 'aud', nếu cần có thể thêm kiểm tra
        )
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=f"Token invalid: {str(e)}")

def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)
