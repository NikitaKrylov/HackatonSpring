
import random

from app.repository.placement import PlacementRepository
from app.repository.product import ProductRepository
from app.repository.supply import SupplyRepository
from app.schemas.filters import PlacementFilter


async def generate_supply(id: int):
    storage_filter = PlacementFilter(placement_type="storage")
    placement_repo = PlacementRepository()
    storage_id = random.choice(await placement_repo.get_all(storage_filter)).id
    supply = {"id": id,
              "storage_id": storage_id}
    return await generate_offer(supply, storage_id)

async def _generate_placement_id(storage_id: int):
    placement_id = storage_id
    placement_repo = PlacementRepository()
    while placement_id == storage_id:
        placement_id = random.choice(await placement_repo.get_all_ids())
    return placement_id

async def generate_offer(supply: dict, storage_id: int):
    product_repo = ProductRepository()
    supply["offers"] =  [{"id": i,
                          "product_count": random.randint(1, 300),
                          "product_id": random.choice(await product_repo.get_all_ids()),
                          "placement_id": await _generate_placement_id(storage_id)} \
                            for i in range(1, random.randint(2, 6))]
    return supply

async def generate_supplies(count: int):
    supply_repo = SupplyRepository()
    data = [await generate_supply(i) for i in range(1, count + 1)]
    await supply_repo.create_all(data)
    # return data
