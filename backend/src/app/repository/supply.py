from app.persistence.sqlalc_models import Offer, Supply
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import SupplyFilter
from app.schemas.supply import SupplyOutDTO


class SupplyRepository(SQLAlchemyRepository):
    model = Supply

    async def get_all(self, filter_data: SupplyFilter | None = None) -> list[SupplyOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                session,
                SupplyOutDTO,
                joins=[Supply.storage],
                eager=[[Supply.offers, Offer.placement], [Supply.offers, Offer.product]],
                filter_data=filter_data
            )

    async def create(self, data: dict):
        async with async_session() as session:
            pass
            #TODO написать создание поставки





