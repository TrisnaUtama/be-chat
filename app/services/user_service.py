from typing import List, Optional

from fastapi.encoders import jsonable_encoder
from sqlmodel import Session, select

from app.models.database import Users
from app.schema.user_schema import UserCreate


class UserService:
    def get(self, db: Session, id: str) -> Optional[Users]:
        return db.get(Users, id)

    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100) -> List[Users]:
        statement = select(Users).offset(skip).limit(limit)
        return db.exec(statement).all()

    def create(self, db: Session, *, obj_in: UserCreate) -> Users:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = Users(**obj_in_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

user_service = UserService()
