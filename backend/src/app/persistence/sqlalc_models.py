from datetime import datetime
from enum import Enum

from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.repository.pg_repository import Base


class SupplyStatus(Enum):
    CANCELED = 'Отменен'
    COMPLETED = 'Выполнен'
    ACTIVE = 'Активный'
    INPROCESSING = 'В обработке'

class User(Base):
    __tablename__ = 'user'

    login: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    role_id: Mapped[int | None] = mapped_column(ForeignKey('role.id'), nullable=True, default=None)
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
    product_amount: Mapped[float]
    product_volume: Mapped[float]
    manufacture_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    expiry_date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    category: Mapped[str] = mapped_column(default='')


class Placement(Base):
    __tablename__ = 'placement'

    name: Mapped[str]
    coord: Mapped[str]
    placement_type: Mapped[str]
    address: Mapped[str]


class Purchase(Base):
    __tablename__ = 'purchase'

    id_store:  Mapped[int] = mapped_column(ForeignKey('placement.id'))
    store: Mapped['Placement'] = relationship(uselist=False)
    id_product: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped['Product'] = relationship(uselist=False)
    time_sale: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    product_cost: Mapped[float]
    quantity_sold: Mapped[float]


class Distance(Base):
    __tablename__ = 'distance'

    source_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    source: Mapped['Placement'] = relationship(foreign_keys=[source_id])
    target_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    target: Mapped['Placement'] = relationship(foreign_keys=[target_id])
    distance: Mapped[float]
    duration: Mapped[float]

# Head
class Supply(Base):
    __tablename__ = 'supply'
    storage_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    storage: Mapped['Placement'] = relationship(uselist=False)
    offers: Mapped[list['Offer']] = relationship()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    supply_status: Mapped[SupplyStatus] = mapped_column(default=SupplyStatus.INPROCESSING)


class Offer(Base):
    __tablename__ = 'offer'

    product_count: Mapped[int]
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    product: Mapped['Product'] = relationship(uselist=False)
    placement_id: Mapped[int] = mapped_column(ForeignKey('placement.id'))
    placement: Mapped['Placement'] = relationship(uselist=False)
    supply_id: Mapped[int] = mapped_column(ForeignKey('supply.id'))

