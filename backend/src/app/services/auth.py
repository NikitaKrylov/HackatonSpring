from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException, Depends
from starlette import status
from app.repository.user import UserRepository
from app.schemas.auth import TokenData
from app.schemas.user import CreateUserDTO, UserOutWithPasswordDTO, UserOutDTO, UserOutWithRoleDTO
from app.shared.logs import get_logger
from app.shared.settings import secure_settings, oauth2_scheme
from app.shared.settings import pwd_context
import os

user_repository = UserRepository()
print(os.listdir('/'))
logger = get_logger(__name__)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(
        to_encode,
        secure_settings.secret_key,
        algorithm=secure_settings.algorithm
    )
    return encoded_jwt


def verify_access_token(token: str):
    credentials_exception = HTTPException(status.HTTP_401_UNAUTHORIZED, 'Не удалось авторизироваться')
    try:
        payload = jwt.decode(token, secure_settings.secret_key, algorithms=[secure_settings.algorithm])
        user_id = payload.get('user_id')

        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except Exception:
        logger.error("Cant verify access token", exc_info=True)
        raise credentials_exception

    return token_data


async def register_user(data: CreateUserDTO):
    data.password = hash_password(data.password)

    return await user_repository.create(data)


async def login_user(username: str, password: str):
    user = await auth_user(username, password)
    access_token = await create_access_token({'user_id': user.id})

    user_data = {
        'access_token': access_token,
        'token_type': 'bearer'
    }
    return user_data


async def auth_user(username: str, password: str):
    user = await user_repository.get_by_login(username, UserOutWithPasswordDTO)

    if not (user and verify_password(password, user.password)):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, 'Неверный логин или пароль.')

    return user


async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserOutDTO:
    token = verify_access_token(token)

    user = await user_repository.get_by_id(token.user_id)

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Не удалось авторизироваться')

    return user


async def get_current_user_with_role(token: str = Depends(oauth2_scheme)) -> UserOutWithRoleDTO:
    token = verify_access_token(token)

    user = await user_repository.get_by_id_with_role(token.user_id)

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Не удалось авторизироваться')

    return user





