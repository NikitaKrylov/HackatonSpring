from pydantic import BaseModel


class BasePlacementDTO(BaseModel):
    product_count: int
    coord: str
    placement_type: str
    address: str


class PlacementOutDTO(BasePlacementDTO):
    id: int


class PlacementCreateDTO(BasePlacementDTO):
    pass
