import enum
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.utils.generate_id import generate_id


class Role(str, enum.Enum):
    ADMIN = "Admin"
    CUSTOMER = "Customer"
    AGENT = "Agent"


class MessageType(str, enum.Enum):
    TEXT = "Text"
    IMAGE = "Image"
    VIDEO = "Video"
    PDF = "PDF"


class RoomParticipants(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    room_id: str = Field(foreign_key="rooms.id")
    user_id: str = Field(foreign_key="users.id")


class Users(SQLModel, table=True):
    id: str = Field(primary_key=True)
    role: Role
    name: str = Field("")

    rooms: List["Rooms"] = Relationship(back_populates="participants", link_model=RoomParticipants)
    messages: List["Messages"] = Relationship(back_populates="sender")


class Rooms(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    name: str = Field(default="Unname")
    image_url: Optional[str] = None

    participants: List[Users] = Relationship(back_populates="rooms", link_model=RoomParticipants)
    messages: List["Messages"] = Relationship(back_populates="room")


class Messages(SQLModel, table=True):
    id: str = Field(default_factory=generate_id, primary_key=True)
    type: MessageType = MessageType.TEXT
    message: str

    room_id: str = Field(foreign_key="rooms.id")
    sender_id: str = Field(foreign_key="users.id")

    room: Rooms = Relationship(back_populates="messages")
    sender: Users = Relationship(back_populates="messages")
