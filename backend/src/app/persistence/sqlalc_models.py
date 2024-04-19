from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.repository.pg_repository import Base


class User(Base):
    __tablename__ = 'users'

    login: Mapped[str]
    password: Mapped[str]
    role_id: Mapped[int | None] = mapped_column(ForeignKey('roles.id'), nullable=True)
    role: Mapped['Role'] = relationship(uselist=False, single_parent=True, back_populates='users')

    def __repr__(self):
        return f'User: {self.login}'


class Role(Base):
    __tablename__ = 'roles'

    name: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
    users: Mapped[User] = relationship(uselist=True, back_populates='role')
    #TODO добавить чекбоксы с разрешениями

