from msgspec import Struct

from app.domain.value_objects import (
    BrewingToolID,
    ToolType,
)


class BrewingTool(Struct):
    id: BrewingToolID
    name: str
    type: ToolType
    is_global: bool

    def make_global(self) -> None:
        self.is_global = True
