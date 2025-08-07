from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from scalar_fastapi import get_scalar_api_reference

from app.core.settings import settings
from app.routes.api import api_router

app = FastAPI(
    title=settings.APP_NAME, docs_url=settings.DOCS_URL, redoc_url=settings.REDOC_URL, openapi_url=settings.OPENAPII_URL
)

if not Path(settings.UPLOADS_DIR).is_absolute():
    app.mount(settings.UPLOADS_URL_PATH, StaticFiles(directory=settings.UPLOADS_DIR), name="uploads")


@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(title=settings.APP_NAME, openapi_url=settings.OPENAPII_URL)


app.include_router(api_router, prefix="/api/v1")
