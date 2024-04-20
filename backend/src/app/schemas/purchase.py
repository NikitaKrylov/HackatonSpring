from datetime import datetime

from pydantic import BaseModel

from app.schemas.supply import PlacementOutDTO, ProductOutDTO


class BasePurchaseDTO(BaseModel):
    id_store: int
    id_product: int
    time_sale: datetime
    product_cost: float
    quantity_sold: float

class PurchaseOutDTO(BasePurchaseDTO):
    id: int
    store: PlacementOutDTO
    product: ProductOutDTO


class PurchaseCreateDTO(BasePurchaseDTO):
    pass
