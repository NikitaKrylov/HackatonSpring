from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.repository.pg_repository import Base


class User(Base):
    __tablename__ = 'user'

    login: Mapped[str]
    password: Mapped[str]
    role_id: Mapped[int | None] = mapped_column(ForeignKey('role.id'), nullable=True)
    role: Mapped['Role'] = relationship(uselist=False, single_parent=True, back_populates='users')

    def __repr__(self):
        return f'User: {self.login}'


class Role(Base):
    __tablename__ = 'role'

    name: Mapped[str]
    is_admin: Mapped[bool] = mapped_column(default=False)
    users: Mapped[User] = relationship(uselist=True, back_populates='role')
    #TODO добавить чекбоксы с разрешениями


class Product(Base):
    __tablename__ = 'product'

    sku: Mapped[int]
    name: Mapped[str]
    manufactor: Mapped[str]
    product_measure: Mapped[str]
    product_amount: Mapped[int]
    product_volume: Mapped[int]
    manufacture_date: Mapped[datetime]
    expiry_date: Mapped[datetime]


class Placement(Base):
    __tablename__ = 'placement'

    name: Mapped[str]
    #TODO check data type 'coord: Mapped[...]'
    coord: Mapped[str]

    placement_type: Mapped[str]


class Purchase(Base):
    __tablename__ = 'purchase'

    id_store:  Mapped[int] = mapped_column(ForeignKey('placement.id'))
    store: Mapped['Placement'] = relationship(uselist=False)
    id_product: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped['Product'] = relationship(uselist=False)
    time_sale: Mapped[datetime]
    product_cost: Mapped[int]
    quantity_sold: Mapped[int]


class ClientInfo(Base):
    __tablename__ = 'client_info'

    client_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    address: Mapped[str]


class Distance(Base):
    __tablename__ = 'distance'

    #TODO обязательно указать back_poppulates c разными именами
    source_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    target_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    distance: Mapped[int]
    duration: Mapped[int]

# Head
class Supply(Base):
    __tablename__ = 'supply'
    storage_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    storage: Mapped['Placement'] = relationship(uselist=False)
    offers: Mapped[list['Offer']] = relationship()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    # TODO сделать статус

class Offer(Base):
    __tablename__ = 'offer'

    product_count: Mapped[int]
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped['Product'] = relationship(uselist=False)
    placement_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    placement: Mapped['Placement'] = relationship(uselist=False)
    supply_id: Mapped[int] = mapped_column(ForeignKey('supply.id'))

