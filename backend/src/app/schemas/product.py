from datetime import datetime

from pydantic import BaseModel


class BaseProductDTO(BaseModel):
    sku: int
    name: str
    manufactor: str
    product_measure: str
    product_amount: float
    product_volume: float
    manufacture_date: datetime
    expiry_date: datetime


class ProductOutDTO(BaseProductDTO):
    id: int


class ProductCreateDTO(BaseProductDTO):
    pass
