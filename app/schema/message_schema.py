from app.models.database import MessageType
from app.schema.base_schema import BaseSchema
from app.schema.user_schema import UserRead


class MessageBase(BaseSchema):
    type: MessageType
    message: str

class MessageCreate(MessageBase):
    sender_id: str

class MessageRead(MessageBase):
    id: str
    sender: UserRead
