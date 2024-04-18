from pydantic_settings import BaseSettings


class Config(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: int

    @property
    def db_url(self) -> str:
        return f'postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.db_host}:{self.db_port}/{self.postgres_db}'


config = Config(_env_file='db.env')
