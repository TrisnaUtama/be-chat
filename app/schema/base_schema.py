from sqlmodel import SQLModel


class BaseSchema(SQLModel):
    class Config:
        from_attributes = True


class UploadResponse(SQLModel):
    file_url: str
