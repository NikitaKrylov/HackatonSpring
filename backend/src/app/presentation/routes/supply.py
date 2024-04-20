from fastapi import APIRouter, Depends

from app.repository.supply import SupplyRepository
from app.schemas.filters import SupplyFilter
from app.schemas.supply import SupplyOutDTO

router = APIRouter(prefix="/supplies")

supply_repository = SupplyRepository()


@router.get('', response_model=list[SupplyOutDTO])
async def get_all_supplies(filter_data: SupplyFilter = Depends(SupplyFilter)):
    return await supply_repository.get_all()


@router.post('')
async def create_supply(data):
    # TODO сделать после того как сделаем метод создания в репозитории
    pass
