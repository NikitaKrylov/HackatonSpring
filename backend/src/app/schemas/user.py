from pydantic import BaseModel


class UserOutDTO(BaseModel):
    id: int
    login: str


class CreateUserDTO(BaseModel):
    login: str
    password: str
    role_id: int | None = None


class UserOutWithPasswordDTO(BaseModel):
    id: int
    login: str
    password: str


class UserRoleChangeDTO(BaseModel):
    id: int
    role_id: int | None


class BaseRoleDTO(BaseModel):
    ...
    #TODO тут перечислять чекбоксы с разрешениями


class RoleOutDTO(BaseRoleDTO):
    id: int
    name: str


class RoleCreateDTO(BaseRoleDTO):
    name: str


class RoleChangeDTO(BaseRoleDTO):
    id: int
    name: str


class UserOutWithRoleDTO(UserOutDTO):
    role: RoleOutDTO | None



