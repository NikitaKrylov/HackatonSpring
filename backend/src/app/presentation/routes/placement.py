from fastapi import APIRouter, Depends

from app.repository.placement import PlacementRepository
from app.schemas.filters import PlacementFilter
from app.schemas.placement import PlacementCreateDTO, PlacementOutDTO

router = APIRouter(prefix='/placements')

placement_repository = PlacementRepository()


@router.get('', response_model=list[PlacementOutDTO])
async def get_all_placements(filter_data: PlacementFilter = Depends(PlacementFilter)):
    return await placement_repository.get_all(filter_data)


@router.post('', response_model=PlacementOutDTO)
async def create_placement(data: PlacementCreateDTO):
    return await placement_repository.create(data)

