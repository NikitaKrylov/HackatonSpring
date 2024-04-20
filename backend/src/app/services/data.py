from io import BytesIO

import pandas as pd
from fastapi import HTTPException, status

from app.repository.product import ProductRepository
from app.schemas.product import ProductCreateDTO

engines = {
        '.xlsx': 'openpyxl',
        '.xls': 'xlrd'
    }

product_repository = ProductRepository()


async def bytes_to_pandas(data: bytes, file_extension: str):
    io = BytesIO(data)

    if file_extension == '.csv':
        return pd.read_csv(io)

    if file_extension not in engines:
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f'Файлы с расширением {file_extension} не поддерживаются')

    return pd.read_excel(io, engine=engines[file_extension])


async def bytes_to_dict(data: bytes):
    # TODO сделать конвертацию json(bytes) в dict
    pass


async def import_placements(data: bytes):
    pass


async def import_products(data: bytes, file_extension: str):
    df = await bytes_to_pandas(data, file_extension)

    df = df[['SKU', 'Product_Name','Manufacturer', 'Product_Measure', 'Product_Amount', 'Product_Volume', 'Manufacture_Date', 'Expiry_Date']]
    df = df.rename({
        'SKU': 'sku',
        'Product_Name': 'name',
        'Manufacturer': 'manufactor',
        'Product_Measure': 'product_measure',
        'Product_Amount': 'product_amount',
        'Product_Volume': 'product_volume',
        'Manufacture_Date': 'manufacture_date',
        'Expiry_Date': 'expiry_date'
    }, axis='columns')

    products = [ProductCreateDTO(**i) for i in df.to_dict('records')][:100]
    await product_repository.create_all(products)


