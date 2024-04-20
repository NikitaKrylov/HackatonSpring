from app.persistence.sqlalc_models import Product
from app.repository.pg_repository import async_session
from app.repository.sqlalchemy_repository import SQLAlchemyRepository
from app.schemas.filters import ProductFilter
from app.schemas.product import ProductCreateDTO, ProductOutDTO


class ProductRepository(SQLAlchemyRepository):
    model = Product

    async def get_all(self, filter_data: ProductFilter | None = None) -> list[ProductOutDTO]:
        async with async_session() as session:
            return await self.get_all_objects(
                filter_data,
                session,
                ProductOutDTO
            )

    async def create(self, data: ProductCreateDTO) -> ProductOutDTO:
        async with async_session() as session:
            return await self.create_object(
                session,
                data,
                ProductOutDTO
            )

    async def create_all(self, data: list[ProductCreateDTO]):
        async with async_session() as session:
            for product in data:
                _obj = self.model(**product.model_dump())
                session.add(_obj)
            await session.commit()
