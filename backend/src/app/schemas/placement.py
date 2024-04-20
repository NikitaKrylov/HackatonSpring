from pydantic import BaseModel


class BasePlacementDTO(BaseModel):
    name: str
    coord: str
    placement_type: str
    address: str


class PlacementOutDTO(BasePlacementDTO):
    id: int
    coord: str | list[float] | list[str]
    capacity: int | None = None
    workload: int | None = None


class PlacementCreateDTO(BasePlacementDTO):
    pass


