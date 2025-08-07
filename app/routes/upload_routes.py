# app/routes/upload_routes.py
from fastapi import APIRouter, File, UploadFile

from app.schema.base_schema import UploadResponse
from app.services.upload_service import upload_service

router = APIRouter()

@router.post("/", response_model=UploadResponse)
def upload_file(file: UploadFile = File(...)):
    file_url = upload_service.save_file(file)
    return {"file_url": file_url}
