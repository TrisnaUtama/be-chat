from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.models.engine import get_session
from app.schema.user_schema import UserCreate, UserRead
from app.services.user_service import user_service

router = APIRouter()

@router.post("/", response_model=UserRead, status_code=201)
def create_user(
    *,
    session: Session = Depends(get_session),
    user_in: UserCreate
):
    user = user_service.get(db=session, id=user_in.id)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Pengguna dengan email ini sudah terdaftar.",
        )

    new_user = user_service.create(db=session, obj_in=user_in)
    return new_user

@router.get("/", response_model=List[UserRead], status_code=200)
def get_users(*, session: Session = Depends(get_session)):
    users = user_service.get_multi(db=session)
    return users

@router.get("/{id}", response_model=UserRead, status_code=200)
def get_user_by_id(*, session:Session = Depends(get_session), id:str):
    user = user_service.get(db=session, id=id)
    return user
