from app.persistence.sqlalc_models import Offer, Supply
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.supply import SupplyOutDTO


class SupplyRepository(SQLAlchemyRepository):
    model = Supply

    async def get_all(self) -> list[SupplyOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                session,
                SupplyOutDTO,
                joins=[Supply.offers, Offer.placement, Offer.product]
            )

    async def create(self, data: dict):
        async with async_session() as session:
            pass
            #TODO написать создание поставки





