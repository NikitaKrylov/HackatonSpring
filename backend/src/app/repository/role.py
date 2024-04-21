from app.persistence.sqlalc_models import Role
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.user import RoleChangeDTO, RoleCreateDTO, RoleOutDTO


class RoleRepository(SQLAlchemyRepository):
    model = Role

    async def get_all(self) -> list[RoleOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                None,
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

    async def update(self, data: list[RoleChangeDTO]) -> None:
        async with async_session() as session:
            for i in data:
                await self.update_object(
                    session,
                    i,
                    self.model.id == i.id
            )

