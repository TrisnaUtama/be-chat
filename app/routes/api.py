
from fastapi import APIRouter

from app.routes import room_routes, upload_routes, user_routes

api_router = APIRouter()

api_router.include_router(user_routes.router, prefix="/users", tags=["Users"])
api_router.include_router(room_routes.router, prefix="/rooms", tags=["Rooms"])
api_router.include_router(upload_routes.router, prefix="/upload", tags=["Upload"])
