from io import BytesIO
import json
import re

import pandas as pd
from fastapi import HTTPException, status

from app.repository.product import ProductRepository
from app.schemas.product import ProductCreateDTO
from app.schemas.placement import PlacementCreateDTO
from app.repository.placement import PlacementRepository

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


async def bytes_to_dict(data: bytes) -> dict:

    return json.loads(data.decode('utf-8'))


async def import_json_data(data: bytes, file_extension: str):
    if not re.match(r"\.[a-zA-Z]*json", file_extension):
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f'Файлы с расширением {file_extension} не поддерживаются')

    data_dict = await bytes_to_dict(data)
    points = data_dict["features"]
    result = map(lambda point: PlacementCreateDTO(name=point["properties"]["iconCaption"],
                                                  coord=f"({point['geometry']['coordinates'][0]}, {point['geometry']['coordinates'][1]})",
                                                  placement_type='storage' if re.match(r"Склад[a-zA-Z0-9\ \-\_*]", point["properties"]["iconCaption"]) else 'client'), points) # type: ignore

    placement_repo = PlacementRepository()
    await placement_repo.create_all(result)


async def import_csv_data(data: bytes, file_extension: str):
    df = await bytes_to_pandas(data, file_extension)

    product_df = df[['SKU', 'Product_Name','Manufacturer', 'Product_Measure', 'Product_Amount', 'Product_Volume', 'Manufacture_Date', 'Expiry_Date']]
    await import_products(product_df)


async def import_placements(dataframe: pd.Series):
    dataframe = dataframe.rename({
        'Store_Name': 'name',
        'Store_Address': 'address',
    }, axis='columns')


async def import_products(dataframe: pd.Series):
    dataframe = dataframe.rename({
        'SKU': 'sku',
        'Product_Name': 'name',
        'Manufacturer': 'manufactor',
        'Product_Measure': 'product_measure',
        'Product_Amount': 'product_amount',
        'Product_Volume': 'product_volume',
        'Manufacture_Date': 'manufacture_date',
        'Expiry_Date': 'expiry_date'
    }, axis='columns')

    products = [ProductCreateDTO(**i) for i in dataframe.to_dict('records')][:100] # type: ignore
    await product_repository.create_all(products)


