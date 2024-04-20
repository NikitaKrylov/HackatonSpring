from pathlib import PurePath

from fastapi import APIRouter, File, UploadFile

from app.services.import_data import import_csv_data, import_json_data

router = APIRouter(prefix="/import")


@router.post('/csv', tags=['import .csv files'])
async def load_csv_data(data: UploadFile = File()):
    content = await data.read()
    await import_csv_data(content, PurePath(data.filename).suffix)

@router.post('/json/placement', tags=['import .json files about placements'])
async def load_json_placement_data(data: UploadFile = File()):
    content = await data.read()
    return await import_json_data(content, PurePath(data.filename).suffix)

@router.post('/json/distance', tags=['import .json files about distances'])
async def load_json_distance_data(data: UploadFile = File()):
    content = await data.read()
    return await import_json_data(content, PurePath(data.filename).suffix)
