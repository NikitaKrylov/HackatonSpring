from pydantic import BaseModel


class BasePlacementDTO(BaseModel):
    name: str
    coord: str
    placement_type: str
    address: str


class PlacementOutDTO(BasePlacementDTO):
    id: int


class PlacementCreateDTO(BasePlacementDTO):
    pass
