from typing import Type

from fastapi import HTTPException
from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status


from app.repository.pg_repository import Base


class SQLAlchemyRepository:
    model: Type[Base] = None

    async def create_object(self, session: AsyncSession,  data: BaseModel, out_schema: Type[BaseModel]):
        _obj = self.model(**data.model_dump())
        session.add(_obj)
        await session.commit()
        await session.refresh(_obj)

        return out_schema.model_validate(_obj, from_attributes=True)

    async def get_object(self, session: AsyncSession, expression, out_schema: Type[BaseModel], allow_none: bool = True, error: HTTPException | None = None, joins: list | None = None):
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

    async def get_all_objects(self, session: AsyncSession, out_schema: Type[BaseModel], joins: list | None = None):
        query = select(self.model)

        if joins is not None:
            for join in joins:
                query = query.options(selectinload(join))

        result = await session.execute(query)
        return [out_schema.model_validate(i, from_attributes=True) for i in result.scalars().all()]

    async def update_object(self, session: AsyncSession, data: BaseModel, expression) -> None:
        stmp = update(self.model).where(expression).values(**data.model_dump())
        await session.execute(stmp)
        await session.commit()

