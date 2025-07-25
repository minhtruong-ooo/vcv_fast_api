from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ENVIRONMENT: str
    KEYCLOAK_URL: str
    KEYCLOAK_REALM: str
    KEYCLOAK_CLIENT_ID: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()