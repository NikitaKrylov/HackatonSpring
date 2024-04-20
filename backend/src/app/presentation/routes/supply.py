from fastapi import APIRouter, Depends

from app.repository.supply import SupplyRepository
from app.schemas.filters import SupplyFilter
from app.schemas.supply import SupplyOutDTO
from app.shared.supply_script import generate_supplies

router = APIRouter(prefix="/supplies")

supply_repository = SupplyRepository()


@router.get('', response_model=list[SupplyOutDTO])
async def get_all_supplies(filter_data: SupplyFilter = Depends(SupplyFilter)):
    return await supply_repository.get_all()


@router.post('', tags=["Для генерации путей в БД"])
async def create_supply(data):
    await generate_supplies(40)
