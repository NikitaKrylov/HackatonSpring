from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.persistence.sqlalc_models import Role
from app.schemas.user import RoleOutDTO, RoleCreateDTO, RoleChangeDTO


class RoleRepository(SQLAlchemyRepository):
    model = Role

    async def get_all(self) -> list[RoleOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                session,
                RoleOutDTO
            )

    async def create(self, data: RoleCreateDTO) -> RoleOutDTO:
        async with async_session() as session:
            return await self.create_object(
                session,
                data,
                RoleOutDTO
            )

    async def update(self, data: RoleChangeDTO) -> None:
        async with async_session() as session:
            await self.update_object(
                session,
                data,
                self.model.id == data.id
            )

