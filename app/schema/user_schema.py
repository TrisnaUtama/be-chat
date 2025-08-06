from typing import Optional

from app.models.database import Role
from app.schema.base_schema import BaseSchema


class UsersBase(BaseSchema):
    id: str
    role: Role
    name: Optional[str] = None

class UserCreate(UsersBase):
    pass

class UserRead(UsersBase):
    pass

class UserInRoom(BaseSchema):
    id:str
