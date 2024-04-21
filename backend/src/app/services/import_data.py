import json
import random
import re
import requests
from io import BytesIO

import pandas as pd
from fastapi import HTTPException, status
from
from app.repository.placement import DistanceRepository, PlacementRepository
from app.repository.product import ProductRepository
from app.schemas.placement import PlacementCreateDTO
from app.shared.settings import secure_settings
from app.schemas.distance import DistanceCreateDTO
from app.schemas.purchase import PurchaseCreateDTO
from app.schemas.product import ProductCreateDTO
from app.repository.purchase import PurchaseRepository
from app.repository.offer import OfferRepository
from backend.src.app.schemas.supply import OfferCreateDTO

engines = {
        '.xlsx': 'openpyxl',
        '.xls': 'xlrd'
    }

_product_repository = ProductRepository()
_placement_repo = PlacementRepository()
_distance_repo = DistanceRepository()
_purchase_repository = PurchaseRepository()


async def bytes_to_pandas(data: bytes, file_extension: str):
    io = BytesIO(data)

    if file_extension == '.csv':
        return pd.read_csv(io)

    if file_extension not in engines:
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f'Файлы с расширением {file_extension} не поддерживаются')

    return pd.read_excel(io, engine=engines[file_extension]) # type: ignore


async def bytes_to_dict(data: bytes) -> dict:

    return json.loads(data.decode('utf-8'))


def get_address_by_coord(coord: str):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    address = coord[1:-1]
    search_params = {
    "text": address,
    "apikey": secure_settings.geocoder_api_key,
    "lang": "ru_RU",
    "type": "geo",
    "results": 1
    }
    response = requests.get(search_api_server, params=search_params)
    result = response.json()
    return result["features"][0]["properties"]["GeocoderMetaData"]["text"]


async def import_json_data(data: bytes, file_extension: str):
    if not re.match(r"\.[a-zA-Z]*json", file_extension):
        raise HTTPException(status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, f'Файлы с расширением {file_extension} не поддерживаются')

    data_dict = await bytes_to_dict(data)
    if file_extension == '.json':
        routes = data_dict["routes"]
        result = [DistanceCreateDTO(source_id=route["source_id"]+1,
                                    target_id=route["target_id"]+1,
                                    distance=route["distance"],
                                    duration=route["duration"],
                                    ) for route in routes ] # type: ignore
        await _distance_repo.create_all(result)
    else:
        points = data_dict["features"]
        result = [PlacementCreateDTO(name=point["properties"]["iconCaption"],
                                     coord=f"({point['geometry']['coordinates'][1]}, {point['geometry']['coordinates'][0]})",
                                     placement_type='storage' if re.match(r"Склад[a-zA-Z0-9\ \-\_*]", point["properties"]["iconCaption"]) else 'client',
                                     address=get_address_by_coord(f"({point['geometry']['coordinates'][1]}, {point['geometry']['coordinates'][0]})")
                                    ) for point in points ] # type: ignore
        await _placement_repo.create_all(result)

    return result


async def import_csv_data(data: bytes, file_extension: str):
    df = await bytes_to_pandas(data, file_extension)

    product_df = df[['SKU', 'Product_Name','Manufacturer', 'Product_Measure', 'Product_Amount', 'Product_Volume', 'Manufacture_Date', 'Expiry_Date']]
    purchase_df = df[['SKU', 'Sale_Date', 'Product_Cost', 'Quantity_Sold']]


    await import_products(product_df)
    await import_purchase(purchase_df)


async def import_products(dataframe: pd.DataFrame):
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
    await _product_repository.create_all(products)
    return 200

async def import_purchase(dataframe: pd.DataFrame):
    acc = 1
    products = []
    for i in dataframe.to_dict('records')[:100]:
        products.append(PurchaseCreateDTO(id_store=random.randint(4, 23),
                                  id_product=acc,
                                  time_sale=i['Sale_Date'],
                                  product_cost=i["Product_Cost"],
                                  quantity_sold=i["Quantity_Sold"]))
        acc += 1
    await _purchase_repository.create_all(products)

async def import_offer_csv(data: bytes, file_extension: str):
    _offer_repo = OfferRepository()
    df = await bytes_to_pandas(data, file_extension)
    offer_df = df[['product_count', 'product_id', 'placement_id', 'supply_id']]

    return await _offer_repo.create_all([OfferCreateDTO(**i) for i in offer_df.to_dict('records')])

async def export_offer_csv(file_name: str = "report.xlsx"):
    _offer_repo = OfferRepository()
    offer_list = await _offer_repo.get_all()
    offers = [offer.model_dump() for offer in offer_list]

    return pd.DataFrame(offers).to_excel(file_name)
