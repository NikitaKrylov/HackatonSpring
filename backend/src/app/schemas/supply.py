
from datetime import datetime

from pydantic import BaseModel

from app.persistence.sqlalc_models import SupplyStatus
from app.schemas.placement import PlacementOutDTO

# -------------- Product ------------------

class BaseProductDTO(BaseModel):
    sku: int
    name: str
    manufactor: str
    product_measure: str
    product_amount: int
    product_volume: int
    manufacture_date: datetime
    expiry_date: datetime


class ProductOutDTO(BaseProductDTO):
    id: int

class ProductCreateDTO(BaseProductDTO):
    pass


# -------------- Offer ------------------

class BaseOfferDTO(BaseModel):
    product_count: int
    product_id: int
    placement_id: int
    supply_id: int


class OfferOutDTO(BaseOfferDTO):
    id: int
    product_count: int
    product: ProductOutDTO
    placement: PlacementOutDTO

class OfferCreateDTO(BaseOfferDTO):
    pass


# -------------- Supply ------------------

class SupplyOutDTO(BaseModel):
    id: int
    storage_id: int
    offers: list[OfferOutDTO]
    created_at: datetime
    supply_status: SupplyStatus





