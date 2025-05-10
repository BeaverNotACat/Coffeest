from typing import Annotated

from msgspec import Meta, Struct

from app.domain.value_objects import (
    Coffee,
    RecipieID,
    UserID,
    WaterPouring,
)

from .brewing_tools import BrewingTool


class Recipe(Struct):
    id: RecipieID
    author: UserID
    tools: Annotated[list[BrewingTool], Meta(min_length=1)]
    coffee: Coffee
    dose: float
    grind: float
    water_temperature: int
    pours: Annotated[list[WaterPouring], Meta(min_length=1)]

    @property
    def total_time(self) -> int:
        return sum(i.time for i in self.pours)

    @property
    def total_water(self) -> int:
        return sum(i.weight for i in self.pours)
