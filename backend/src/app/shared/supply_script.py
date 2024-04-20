
import random
from random import random

from app.repository.placement import PlacementRepository
from app.schemas.filters import PlacementFilter


def generate_supply(id: int):
    storage_filter = PlacementFilter(placement_type="storage")
    placement_repo = PlacementRepository()
    storage_id = random.choice(placement_repo.get_all(storage_filter))[0]
    supply = {"id": id,
              "storage_id": storage_id}
    return generate_offer(supply, storage_id)

def _generate_placement_id(storage_id: int):
    placement_id = storage_id
    placement_repo = PlacementRepository()
    while placement_id == storage_id:
        placement_id = random.choice(placement_repo.get_all())[0]
    return placement_id

def generate_offer(supply: dict, storage_id: int):

    supply["offers"] =  [{"id": i,
                          "product_count": random.randint(1, 300),
                          "product_id": random.choice(),
                          "placement_id": _generate_placement_id(storage_id)} \
                            for i in range(1, random.randint(2, 6))]
    return supply

def generate_supplies(count: int):
    data = [generate_supply(i) for i in range(1, count + 1)]
    # TODO: add CRUD for models
    return data
