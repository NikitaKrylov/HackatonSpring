from sqlalchemy.orm import Mapped

from app.repository.pg_repository import Base


class User(Base):
    __tablename__ = 'users'

    login: Mapped[str]
    password: Mapped[str]

    def __repr__(self):
        return f'User: {self.login}'
