from pydantic import BaseModel

from app.schemas.placement import PlacementOutDTO


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
