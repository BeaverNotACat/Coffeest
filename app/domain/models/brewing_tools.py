from msgspec import Struct

from app.domain.value_objects import (
    BrewingMethod,
    BrewingToolID,
)


class BrewingTool(Struct):
    id: BrewingToolID
    name: str
    type: BrewingMethod
    is_global: bool
