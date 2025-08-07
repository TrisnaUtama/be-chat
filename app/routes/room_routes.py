from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.models.engine import get_session
from app.schema.room_schema import RoomCreate, RoomRead
from app.services.room_service import room_service

router = APIRouter()

@router.post("/", response_model=RoomRead, status_code=201)
def create_room(
    *,
    session: Session = Depends(get_session),
    room_in: RoomCreate
):
    try:
        room = room_service.create(db=session, obj_in=room_in)
        return room_service.get(db=session, id=room.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[RoomRead])
def get_all_rooms(
    *,
    session: Session = Depends(get_session)
):
    rooms = room_service.get_multi(db=session)
    return rooms

@router.get("/{room_id}", response_model=RoomRead)
def get_room_by_id(
    room_id: str,
    *,
    session: Session = Depends(get_session)
):
    room = room_service.get(db=session, id=room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room tidak ditemukan")
    return room
