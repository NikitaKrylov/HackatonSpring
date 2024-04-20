from sqlalchemy import text

from app.persistence.sqlalc_models import Purchase
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import PurchaseFilter
from app.schemas.purchase import PurchaseCreateDTO, PurchaseOutDTO


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
            query = """SELECT product.category,
            CAST (sum(purchase.quantity_sold) as FLOAT) /
            (SELECT sum(purchase.quantity_sold) FROM product RIGHT OUTER JOIN purchase ON purchase.id_product = product.id)
            FROM purchase JOIN product ON purchase.id_product = product.id GROUP BY product.category"""
            return {i[0]: i[1] for i in (await session.execute(text(query))).fetchall()}


    async def _get_turnover_per_last_week_by_category(self, category: str):
        async with async_session() as session:
            category = 'а'
            query = f"""SELECT
            date_part('week', date(supply.created_at)) as week,
            count(offer.id)
            FROM supply
            JOIN offer ON offer.supply_id = supply.id
            JOIN product ON product.id = offer.product_id
            WHERE product.category = '{category}'
            GROUP BY week"""
            return [{
                'week': i[0],
                'value': i[1]
            } for i in (await session.execute(text(query))).fetchall()]

    async def get_purches_stats(self, category: str):
        return {
            'turnover': await self._get_turnover_per_last_week_by_category(category),
            'categories': await self._get_categories_stat()
        }
