from typing import Type

from app.persistence.sqlalc_models import User
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.user import (
    CreateUserDTO,
    UserOutDTO,
    UserOutWithPasswordDTO,
    UserOutWithRoleDTO,
    UserRoleChangeDTO,
)


class UserRepository(SQLAlchemyRepository):
    model = User

    async def create(self, data: CreateUserDTO) -> UserOutDTO:
        async with async_session() as session:
            return await self.create_object(
                session,
                data,
                UserOutDTO
            )

    async def get_by_id(self, _id: int) -> UserOutDTO | None:
        async with async_session() as session:
            return await self.get_object(
                session,
                self.model.id == _id,
                UserOutDTO
            )

    async def get_by_id_with_role(self, _id: int) -> UserOutWithRoleDTO | None:
        async with async_session() as session:
            return await self.get_object(
                session,
                self.model.id == _id,
                UserOutWithRoleDTO,
                joins=[self.model.role]
            )

    async def get_by_login(self, login: str, out_schema: Type[UserOutDTO | UserOutWithPasswordDTO] = UserOutDTO) -> UserOutDTO | None | UserOutWithPasswordDTO:
        async with async_session() as session:
            return await self.get_object(
                session,
                self.model.login == login,
                out_schema
            )

    async def set_roles(self, data: list[UserRoleChangeDTO]) -> None:
        async with async_session() as session:
            for i in data:
                await self.update_object(
                    session,
                    i,
                    self.model.id == i.id
                )

    async def get_all(self) -> list[UserOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                None,
                session,
                UserOutDTO
            )

