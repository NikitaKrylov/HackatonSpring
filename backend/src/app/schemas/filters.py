

from abc import ABC

from pydantic import BaseModel

from app.persistence.sqlalc_models import SupplyStatus


class BaseFilterData(BaseModel, ABC):
    def get_filters(self):
        return {key: value for key, value in self.model_dump().items() if value is not None}

    @classmethod
    def default(cls):
        return cls()


class SupplyFilter(BaseFilterData):
    supply_status: SupplyStatus | None = None

