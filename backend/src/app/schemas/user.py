from pydantic import BaseModel


class UserOutDTO(BaseModel):
    id: int
    login: str
    first_name: str
    last_name: str
    middle_name: str
    phone: str


class CreateUserDTO(BaseModel):
    login: str
    password: str
    first_name: str
    last_name: str
    middle_name: str
    phone: str
    role_id: int | None = None


class UserOutWithPasswordDTO(BaseModel):
    id: int
    login: str
    password: str
    first_name: str
    last_name: str
    middle_name: str
    phone: str


class UserRoleChangeDTO(BaseModel):
    id: int
    role_id: int | None


class BaseRoleDTO(BaseModel):
    is_admin: bool


class RoleOutDTO(BaseRoleDTO):
    id: int
    name: str


class RoleCreateDTO(BaseRoleDTO):
    name: str


class RoleChangeDTO(BaseRoleDTO):
    id: int
    name: str
    is_admin: bool


class UserOutWithRoleDTO(UserOutDTO):
    role: RoleOutDTO | None



