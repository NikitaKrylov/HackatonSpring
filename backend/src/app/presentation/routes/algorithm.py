import json
import os
from fastapi import APIRouter, HTTPException

from app.services.path_algorithm import get_routes
from app.repository.supply import SupplyRepository


router = APIRouter(prefix="/algorithms")

_supply_repository = SupplyRepository()

@router.get("/algorithm_graph")
async def optimal_path(supply_id: int, num_trucks: int = 1):
    supply = await _supply_repository.get_supply_by_id(supply_id)
    storage_id = supply.id - 1 # type: ignore
    clients_id = [i.placement_id - 1 for i in supply.offers] # type: ignore
    if len(clients_id) < num_trucks:
        raise HTTPException(status_code=400, detail="Number of trucks must be greater than or equal to the number of clients")

    with open(os.path.abspath("data/points.geojson"), 'r') as f:
        points_json = json.load(f)

    with open(os.path.abspath("data/routes.json"), 'r') as f:
        routes_json = json.load(f)

    result = await get_routes(storage_id, clients_id, points_json, routes_json, num_trucks=num_trucks)
    print([[j+1 for j in i] for i in result])
    result =[[j+1 for j in i] for i in result]
    return result
