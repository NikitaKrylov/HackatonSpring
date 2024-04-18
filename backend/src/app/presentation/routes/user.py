from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.repository.user import UserRepository
from app.schemas.user import CreateUserDTO, UserOutDTO
from app.services.auth import get_current_user
from app.services import auth
from app.schemas.auth import Token

router = APIRouter(prefix="/users")


user_repository = UserRepository()


@router.post('/login', response_model=Token)
async def login_user(login_form: OAuth2PasswordRequestForm = Depends()):
    token = await auth.login_user(login_form.username, login_form.password)
    return token


@router.post('/register', response_model=UserOutDTO)
async def create_user(data: CreateUserDTO):
    return await auth.register_user(data)


@router.post('/me', response_model=UserOutDTO | None)
async def get_active_user(current_user=Depends(get_current_user)):
    return current_user
