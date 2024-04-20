from app.persistence.sqlalc_models import Purchase
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import PurchaseFilter
from app.schemas.purchase import PurchaseOutDTO


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase

    async def get_all(self, filter_data: PurchaseFilter) -> list[PurchaseOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                filter_data,
                session,
                PurchaseOutDTO,
                joins=[Purchase.store, Purchase.product]
            )

    async def create(self, data):
        async with async_session() as session:
            pass
            # TODO написать

