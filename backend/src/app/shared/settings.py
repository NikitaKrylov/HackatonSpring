from fastapi.security import OAuth2PasswordBearer
from pydantic_settings import BaseSettings
from passlib.context import CryptContext


class SecureSettings(BaseSettings):
    algorithm: str
    secret_key: str


secure_settings = SecureSettings()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/users/login')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

