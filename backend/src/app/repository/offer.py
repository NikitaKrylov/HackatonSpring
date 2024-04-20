from typing import Iterable

from app.persistence.sqlalc_models import Offer
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import OfferFilter
from app.schemas.supply import OfferCreateDTO, OfferOutDTO


class OfferRepository(SQLAlchemyRepository):
    model = Offer

    async def get_all(self, filter_data: OfferFilter | None = None) -> list[OfferOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                filter_data,
                session,
                OfferOutDTO,
                joins=[Offer.placement, Offer.product]
            ) # type: ignore

    async def create(self, data: OfferCreateDTO):
        async with async_session() as session:
            return await self.create_object(
                session,
                data,
                OfferOutDTO
            )

    async def create_all(self, data: Iterable[OfferCreateDTO]):
        async with async_session() as session:
            for placement in data:
                _obj = self.model(**placement.model_dump())
                session.add(_obj)
            await session.commit()

