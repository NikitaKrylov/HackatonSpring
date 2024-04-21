from fastapi import APIRouter, Depends

from app.repository.supply import SupplyRepository
from app.schemas.filters import SupplyFilter
from app.schemas.supply import SupplyOutDTO
from app.shared.supply_script import generate_supplies

router = APIRouter(prefix="/supplies")

_supply_repository = SupplyRepository()


@router.get('', response_model=list[SupplyOutDTO])
async def get_all_supplies(filter_data: SupplyFilter = Depends(SupplyFilter)):
    supplies = await _supply_repository.get_all()
    for supply in supplies:
        supply.storage.coord = list(reversed([float(coord) for coord in supply.storage.coord[1:-1].split(',')])) # type: ignore
    return supplies


@router.get('/{id}', response_model=SupplyOutDTO)
async def get_supply(id: int):
    return await _supply_repository.get_supply_by_id(id)



@router.post('', tags=["Для генерации путей в БД"])
async def create_supply(amount: int = 40):
    rez =  await generate_supplies(amount)
    return rez
