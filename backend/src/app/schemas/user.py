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

    can_edit_users: bool = False
    can_read_users: bool = False
    can_edit_roles: bool = False
    can_manage_roles: bool = False
    cat_edit_supply: bool = False
    can_read_supply: bool = False
    can_edit_offers: bool = False
    can_read_offers: bool = False
    can_read_statistic: bool = False


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



