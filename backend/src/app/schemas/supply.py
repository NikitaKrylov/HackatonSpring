
from datetime import datetime

from matplotlib.pylab import f
from pydantic import BaseModel

from app.persistence.sqlalc_models import SupplyStatus
from app.schemas.placement import PlacementOutDTO

# -------------- Product ------------------

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

class SimpleOfferOutDTO(BaseModel):
    id: int
    product_count: int
    product_id: int
    placement_id: int
    supply_id: int

class SimplePlacementOutDTO(BaseModel):
    address: str
    name: str
    id: int
    coord: str | list[float] | list[str]
    placement_type: str

class SupplyOutDTO(BaseModel):
    id: int
    storage_id: int
    offers: list[SimpleOfferOutDTO]
    storage: SimplePlacementOutDTO
    created_at: datetime
    supply_status: SupplyStatus
    transport_date: datetime | None = None


class SupplyCreateDTO(BaseModel):
    storage_id: int
    offers: list[OfferOutDTO]
    supply_status: SupplyStatus




