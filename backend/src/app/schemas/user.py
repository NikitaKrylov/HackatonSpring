from pydantic import BaseModel


class UserOutDTO(BaseModel):
    id: int
    login: str


class CreateUserDTO(BaseModel):
    login: str
    password: str


class UserOutWithPasswordDTO(BaseModel):
    id: int
    login: str
    password: str



