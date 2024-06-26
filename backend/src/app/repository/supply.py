from datetime import timedelta
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.persistence.sqlalc_models import Offer, Supply, SupplyStatus
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import SupplyFilter
from app.schemas.supply import SupplyOutDTO


class SupplyRepository(SQLAlchemyRepository):
    model = Supply


    async def get_all(self, filter_data: SupplyFilter | None = None):
        async with async_session() as session:
            query = select(Supply).options(
                selectinload(Supply.offers),
                selectinload(Supply.storage),
            )
            result = await session.execute(query)
            r = [SupplyOutDTO.model_validate(i, from_attributes=True) for i in result.scalars().unique().all()]
            for _ in r:
                _.transport_date = _.created_at + timedelta(days=7)
            return r

    async def get_supply_by_id(self, supply_id: int) -> SupplyOutDTO | None:
        async with async_session() as session:
            query = select(Supply).options(
                selectinload(Supply.offers),
                selectinload(Supply.storage),
            ).where(Supply.id == supply_id)
            result = await session.execute(query)
            r = SupplyOutDTO.model_validate(result.scalar_one_or_none(), from_attributes=True)
            r.transport_date = r.created_at + timedelta(days=7)
            return r

    async def create_all(self, data: list[dict]):
        async with async_session() as session:
            for supply in data:
                _obj = self.model(storage_id=supply['storage_id'], supply_status=SupplyStatus.ACTIVE)
                session.add(_obj)
                await session.commit()
                await session.refresh(_obj)

                session.add_all([
                    Offer(
                        product_count=offer['product_count'],
                        product_id=offer['product_id'],
                        placement_id=offer['placement_id'],
                        supply_id=_obj.id
                          ) for offer in supply['offers']
                ])
                await session.commit()







