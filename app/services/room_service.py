from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select

from app.models.database import Rooms, Users
from app.schema.room_schema import RoomCreate


class RoomService:
    def get(self, db:Session, id:str) -> Optional[Rooms]:
        statetment = (
            select(Rooms)
            .where(Rooms.id == id)
            .options(
                selectinload(Rooms.participants),
                selectinload(Rooms.messages)
            )
        )
        return db.exec(statetment).first()

    def get_multi(self, db:Session, skip: int = 0, limit: int = 100) -> List[Rooms]:
        statement = select(Rooms).offset(skip).limit(limit).options( selectinload(Rooms.participants),
                selectinload(Rooms.messages))
        return db.exec(statement). all()

    def create(self, db:Session, obj_in: RoomCreate) -> Rooms:
        obj_in_data = jsonable_encoder(obj_in, exclude={"participants"})
        db_obj = Rooms(**obj_in_data)

        participant_ids = [p.id for p in obj_in.participant]
        if not participant_ids:
            raise ValueError("Room harus memiliki minimal i peserta")

        statement = select(Users).where(Users.id.in_(participant_ids))
        participants_in_db = db.exec(statement).all()

        if len(participants_in_db) != len(participant_ids):
            raise ValueError("ID peserta tidak ditemukan di database.")

        db_obj.participants.extend(participants_in_db)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

room_service = RoomService()
