from typing import Iterable

from app.persistence.sqlalc_models import Distance, Placement
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.distance import DistanceCreateDTO, DistanceOutDTO
from app.schemas.filters import PlacementFilter
from app.schemas.placement import (
    PlacementCreateDTO,
    PlacementOutDTO,
)


class PlacementRepository(SQLAlchemyRepository):
    model = Placement

    async def get_all(self, filter_data: PlacementFilter | None = None) -> list[PlacementOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                filter_data,
                session,
                PlacementOutDTO
            ) # type: ignore

    async def create(self, data: PlacementCreateDTO):
        async with async_session() as session:
            return await self.create_object(
                session,
                data,
                PlacementOutDTO
            )

    async def create_all(self, data: Iterable[PlacementCreateDTO]):
        async with async_session() as session:
            for placement in data:
                _obj = self.model(**placement.model_dump())
                session.add(_obj)
            await session.commit()


class DistanceRepository(SQLAlchemyRepository):
    model = Distance

    async def get_all(self, filter_data):
        async with async_session() as session:
            return await self.get_all_objects(
                filter_data,
                session,
                DistanceOutDTO,
                joins=[Distance.source, Distance.target]
            )

    async def create_all(self, data: Iterable[DistanceCreateDTO]) -> None:
        async with async_session() as session:
            for distance in data:
                _obj = self.model(**distance.model_dump())
                session.add(_obj)
            await session.commit()
