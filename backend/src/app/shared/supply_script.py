
import random

from app.repository.placement import PlacementRepository
from app.repository.product import ProductRepository
from app.repository.supply import SupplyRepository
from app.repository.offer import OfferRepository
from app.schemas.filters import PlacementFilter

ACC = 1

async def generate_supply(id: int):
    storage_filter = PlacementFilter(placement_type="storage")
    placement_repo = PlacementRepository()
    storage_id = random.choice(await placement_repo.get_all(storage_filter)).id
    active_points=[storage_id]
    supply = {"id": id,
              "storage_id": storage_id}

    placement_repo = PlacementRepository()
    placements_ids = await placement_repo.get_all_ids()
    return await generate_offer(supply, storage_id, active_points)

async def _generate_placement_id(storage_id: int):
    placement_id = storage_id
    placement_repo = PlacementRepository()
    while placement_id == storage_id:
        placement_id = random.choice(await placement_repo.get_all_ids())
    return placement_id

async def generate_offer(supply: dict, storage_id: int, active_points: list):
    product_repo = ProductRepository()

    supply["offers"] = []
    for i in range(random.randint(4, 8)):
        while (placement_id := await _generate_placement_id(storage_id)) in active_points:
            pass
        active_points.append(placement_id)
        supply["offers"].append({"product_count": random.randint(1, 300),
                                 "product_id": random.choice(await product_repo.get_all_ids()),
                                 "placement_id": placement_id})
    return supply

async def generate_supplies(count: int):
    supply_repo = SupplyRepository()
    data = [await generate_supply(i) for i in range(1, count + 1)]
    await supply_repo.create_all(data)
    # return data
