from fastapi import APIRouter

from app.repository.purchase import PurchaseRepository
from app.schemas.purchase import PurchaseOutDTO

router = APIRouter(prefix="/purchases")

purchase_repository = PurchaseRepository()


@router.get('', response_model=list[PurchaseOutDTO])
async def get_all_purchases():
    return await purchase_repository.get_all()


@router.post('', response_model=PurchaseOutDTO)
async def create_purchase():
    # TODO надо сделать
    pass
