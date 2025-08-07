from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    DOCS_URL: Optional[str] = None
    REDOC_URL: Optional[str] = None
    OPENAPII_URL: str = "/openapi.json"
    SCALAR_URL: str = "/scalar"
    DATABASE_URL: str
    UPLOADS_DIR: str
    UPLOADS_URL_PATH:str
    BASE_URL: str

    class Config:
        env_file = ('.env.local', '.env.production')
        extra = "ignore"


settings = Settings()

print("--- DEBUG SETTINGS ---")
print(f"Uploads Dir: {settings.UPLOADS_DIR}")
print(f"Base URL: {settings.BASE_URL}")
print("----------------------")
