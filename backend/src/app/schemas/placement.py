from pydantic import BaseModel


class BasePlacementDTO(BaseModel):
    name: str
    coord: str
    placement_type: str


class PlacementOutDTO(BasePlacementDTO):
    id: int


class PlacementCreateDTO(BasePlacementDTO):
    pass


class BaseDistanceDTO(BaseModel):
    source_id: int
    target_id: int
    distance: float
    duration: float


class DistanceOutDTO(BaseDistanceDTO):
    id: int
    source: PlacementOutDTO
    target: PlacementOutDTO


class DistanceCreateDTO(BaseDistanceDTO):
    pass
