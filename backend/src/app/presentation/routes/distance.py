from fastapi import APIRouter, Depends

from app.repository.placement import DistanceRepository
from app.schemas.filters import PlacementFilter
from app.schemas.distance import DistanceOutDTO

router = APIRouter(prefix='/distance')

distance_repository = DistanceRepository()


@router.get('', response_model=list[DistanceOutDTO])
async def get_all_distances(filter_data: PlacementFilter = Depends(PlacementFilter)):
    return await distance_repository.get_all(filter_data)

