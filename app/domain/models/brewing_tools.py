from msgspec import Struct

from app.domain.value_objects import (
    BrewingMethod,
    BrewingToolID,
)


class BrewingTool(Struct):
    id: BrewingToolID
    name: str
    method: BrewingMethod | None
    is_global: bool

    def make_global(self) -> None:
        self.is_global = True
