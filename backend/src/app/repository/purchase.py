from app.persistence.sqlalc_models import Purchase
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.purchase import PurchaseOutDTO


class PurchaseRepository(SQLAlchemyRepository):
    model = Purchase

    async def get_all(self) -> list[PurchaseOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                session,
                PurchaseOutDTO,
                joins=[Purchase.store, Purchase.product]
            )

    async def create(self, data):
        async with async_session() as session:
            pass
            # TODO написать

