from pathlib import PurePath

from fastapi import APIRouter, Depends, File, UploadFile

from app.repository.purchase import PurchaseRepository
from app.schemas.filters import PurchaseFilter
from app.schemas.purchase import PurchaseOutDTO
from app.services.data import bytes_to_pandas

router = APIRouter(prefix="/purchases")

purchase_repository = PurchaseRepository()


@router.get('', response_model=list[PurchaseOutDTO])
async def get_all_purchases(filter_data: PurchaseFilter = Depends(PurchaseFilter)):
    return await purchase_repository.get_all(filter_data)


@router.post('', response_model=PurchaseOutDTO)
async def create_purchase():
    # TODO надо сделать
    pass


@router.post('/import')
async def import_purchases(data: UploadFile = File()):
    content = await data.read()
    df = await bytes_to_pandas(content, PurePath(data.filename).suffix)

    # TODO написать функцию создания объектов бд из датафрейма, использую bytes_to_pandas
