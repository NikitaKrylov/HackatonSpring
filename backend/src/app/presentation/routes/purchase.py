
from fastapi import APIRouter, Depends

from app.repository.purchase import PurchaseRepository
from app.schemas.filters import PurchaseFilter
from app.schemas.purchase import PurchaseOutDTO

router = APIRouter(prefix="/purchases")

purchase_repository = PurchaseRepository()


@router.get('', response_model=list[PurchaseOutDTO])
async def get_all_purchases(filter_data: PurchaseFilter = Depends(PurchaseFilter)):
    return await purchase_repository.get_all(filter_data)


@router.get('/statistic')
async def test_category_stat(category: str):
    return await purchase_repository.get_purches_stats(category)

