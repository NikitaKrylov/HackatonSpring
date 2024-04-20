from fastapi import APIRouter, Depends

from app.repository.purchase import PurchaseRepository
from app.schemas.filters import PurchaseFilter
from app.schemas.purchase import PurchaseOutDTO

router = APIRouter(prefix="/purchases")

_offer_repository = OfferRepository()


@router.get('', response_model=list[PurchaseOutDTO])
async def get_all_offers(filter_data: PurchaseFilter = Depends(PurchaseFilter)):
    return await _offer_repository.get_all(filter_data)

