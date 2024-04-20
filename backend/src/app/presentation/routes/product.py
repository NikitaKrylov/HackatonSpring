from pathlib import PurePath

from fastapi import APIRouter, Depends, File, UploadFile

from app.repository.product import ProductRepository
from app.schemas.filters import ProductFilter
from app.schemas.product import ProductCreateDTO, ProductOutDTO
from app.services.data import import_products

router = APIRouter(prefix='/products')

product_repository = ProductRepository()


@router.get('', response_model=list[ProductOutDTO])
async def get_all_products(filter_data: ProductFilter = Depends(ProductFilter)):
    return await product_repository.get_all(filter_data)


@router.post('', response_model=ProductOutDTO)
async def create_product(data: ProductCreateDTO):
    return await product_repository.create(data)


@router.post('/import')
async def import_products_data(data: UploadFile = File()):
    content = await data.read()
    await import_products(content, PurePath(data.filename).suffix)
