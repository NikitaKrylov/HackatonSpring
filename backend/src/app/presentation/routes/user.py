from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.repository.user import UserRepository
from app.schemas.auth import Token
from app.schemas.user import (
    CreateUserDTO,
    UserOutDTO,
    UserOutWithRoleDTO,
    UserRoleChangeDTO,
)
from app.services import auth
from app.services.auth import get_current_user_with_role

router = APIRouter(prefix="/users")


user_repository = UserRepository()


@router.get('', response_model=list[UserOutWithRoleDTO])
async def get_all_users():
    return await user_repository.get_all()

@router.delete('/{user_id}')
async def delete_user(user_id: int):
    await user_repository.delete(user_id)

@router.post('/login', response_model=Token)
async def login_user(login_form: OAuth2PasswordRequestForm = Depends()):
    token = await auth.login_user(login_form.username, login_form.password)
    return token


@router.post('/register', response_model=UserOutDTO)
async def create_user(data: CreateUserDTO):
    return await auth.register_user(data)


@router.post('/me', response_model=UserOutWithRoleDTO | None)
async def get_active_user(current_user=Depends(get_current_user_with_role)):
    return current_user


@router.post('/roles')
async def set_users_roles(data: list[UserRoleChangeDTO]):
    await user_repository.set_roles(data)

