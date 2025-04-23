from uuid import uuid4

from app.domain.models.brewing_tools import BrewingTool
from app.domain.value_objects import BrewingMethod, BrewingToolID


class BrewingToolService:
    def create_brewing_tool(
        self, name: str, method: BrewingMethod | None
    ) -> BrewingTool:
        return BrewingTool(
            id=BrewingToolID(uuid4()),
            name=name,
            method=method,
            is_global=False,
        )
