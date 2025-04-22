from typing import Annotated

from msgspec import Meta, Struct

from app.domain.value_objects import (
    Coffee,
    RecipieID,
    UserID,
    WaterPouring,
)

from .brewing_tools import BrewingTool


class Recipie(Struct):
    id: RecipieID
    user: UserID
    coffee: Coffee
    water_temperature: int
    brewing_tool: BrewingTool
    pours: Annotated[list[WaterPouring], Meta(min_length=1)]

    @property
    def total_time(self) -> int:
        return sum(i.time for i in self.pours)
