from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    DOCS_URL: Optional[str] = None
    REDOC_URL: Optional[str] = None
    OPENAPII_URL: str = "/openapi.json"
    SCALAR_URL: str = "/scalar"
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
