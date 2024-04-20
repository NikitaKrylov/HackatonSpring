from typing import Any, Type

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import contains_eager, selectinload
from starlette import status

from app.repository.pg_repository import Base, async_session
from app.schemas.filters import BaseFilterData


class SQLAlchemyRepository:
    model: Type[Base] = None

    async def create_object(self, session: AsyncSession,  data: BaseModel, out_schema: Type[BaseModel]):
        _obj = self.model(**data.model_dump())
        session.add(_obj)
        await session.commit()
        await session.refresh(_obj)

        return out_schema.model_validate(_obj, from_attributes=True)

    async def get_object(self,
                         session: AsyncSession,
                         expression,
                         out_schema: Type[BaseModel],
                         allow_none: bool = True,
                         error: HTTPException | None = None,
                         joins: list | None = None):
        query = select(self.model).where(expression)

        if joins is not None:
            for join in joins:
                query = query.options(selectinload(join))

        result = await session.execute(query)

        _obj = result.scalar_one_or_none()

        if _obj is None:
            if not allow_none:
                raise error or HTTPException(status_code=status.HTTP_404_NOT_FOUND)

            return _obj

        return out_schema.model_validate(_obj, from_attributes=True)

    async def get_all_objects(self,
                              filter_data: BaseFilterData | None,
                              session: AsyncSession,
                              out_schema: Type[BaseModel],
                              joins: list | None = None,
                              eager: list[list[Any]] | None = None
                              ):
        query = select(self.model)

        if joins is not None:
            for join in joins:
                query = query.options(selectinload(join))

        if eager:
            for i in eager:
                query = query.options(contains_eager(*i))

        if filter_data:
            query = query.filter_by(**filter_data.get_filters())

        result = await session.execute(query)
        return [out_schema.model_validate(i, from_attributes=True) for i in result.scalars().all()]

    async def update_object(self, session: AsyncSession, data: BaseModel, expression) -> None:
        stmp = update(self.model).where(expression).values(**data.model_dump())
        await session.execute(stmp)
        await session.commit()


    async def get_all_ids(self) -> list[int]:
        async with async_session() as session:
            query = select(self.model.id)
            result = await session.execute(query)
            return [i[0] for i in result.all()]



