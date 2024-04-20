from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import text

from app.shared.config import config

engine = create_async_engine(
    config.db_url,
    future=True,
    echo=False,
    pool_pre_ping=True
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement=True, unique=True, primary_key=True, index=True)


async_session = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def healthcheck():
    async with async_session() as session:
        await session.execute(text("SELECT 1"))

