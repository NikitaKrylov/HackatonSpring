from sqlalchemy import func, select
from sqlalchemy.orm import selectinload

from app.persistence.sqlalc_models import Purchase
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import PurchaseFilter
from app.schemas.purchase import PurchaseOutDTO, PurchaseCreateDTO


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

    async def create_all(self, data: list[PurchaseCreateDTO]):
        async with async_session() as session:
            for i in data:
                _obj = self.model(**i.model_dump())
                session.add(_obj)
            await session.commit()





    async def _get_categories_stat(self):
        async with async_session() as session:
            query = select(Purchase.product.category, func.count(Purchase.product.id))\
                .group_by(Purchase.product.category)\
                .options(selectinload(Purchase.product))
            result = await session.execute(query)

            return result.all()



