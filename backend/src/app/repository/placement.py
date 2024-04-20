from app.persistence.sqlalc_models import Placement
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import PlacementFilter
from app.schemas.purchase import PlacementOutDTO
from app.repository.pg_repository import async_session


class PlacementRepository(SQLAlchemyRepository):
    model = Placement

    async def get_all(self, filter_data: PlacementFilter | None = None) -> list[PlacementOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                filter_data=filter_data,
                session,
                PlacementOutDTO
            )

    async def create(self, data):
        async with async_session() as session:
            pass
            # TODO написать
