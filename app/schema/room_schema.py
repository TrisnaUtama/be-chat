from typing import List, Optional

from app.schema.base_schema import BaseSchema
from app.schema.message_schema import MessageRead
from app.schema.user_schema import UserInRoom, UserRead


class RoomBase(BaseSchema):
    name: str
    is_group: bool = True

class RoomCreate(RoomBase):
    participant: List[UserInRoom]

class RoomRead(RoomBase):
    id: str
    image_url: Optional[str] = None
    participants : List[UserRead] = []
    messages: List[MessageRead] = []
