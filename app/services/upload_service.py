import uuid
from pathlib import Path

from fastapi import UploadFile

from app.core.settings import settings


class UploadService:
    def save_file(self, file: UploadFile) -> str:
        upload_dir = Path(settings.UPLOADS_DIR)
        upload_dir.mkdir(parents=True, exist_ok=True)

        file_extension = Path(file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_extension}"

        file_path = upload_dir / unique_filename

        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        url_path = f"{settings.UPLOADS_URL_PATH.rstrip('/')}/{unique_filename}"

        return f"{settings.BASE_URL.rstrip('/')}{url_path}"

upload_service = UploadService()
