import random
from fastapi import APIRouter, Depends

from app.repository.placement import PlacementRepository
from app.schemas.filters import PlacementFilter
from app.schemas.placement import PlacementCreateDTO, PlacementOutDTO

router = APIRouter(prefix='/placements')

placement_repository = PlacementRepository()


@router.get('', response_model=list[PlacementOutDTO])
async def get_all_placements(filter_data: PlacementFilter = Depends(PlacementFilter)):

    placements = await placement_repository.get_all(filter_data)
    for placement in placements:
        placement.coord = list(reversed([float(coord) for coord in placement.coord[1:-1].split(',')])) # type: ignore
        if 1 <= placement.id <= 3:
            placement.capacity = random.randint(2300, 2500)
            placement.workload = random.randint(1000, 2000)
    return placements


@router.post('', response_model=PlacementOutDTO)
async def create_placement(data: PlacementCreateDTO):
    return await placement_repository.create(data)

