
from fastapi import APIRouter

from app.presentation.routes.user import router as user_router
from app.presentation.routes.role import router as role_router


api_router = APIRouter(prefix="/api")

api_router.include_router(user_router, tags=["Пользователь"])
api_router.include_router(role_router, tags=['Роли'])
