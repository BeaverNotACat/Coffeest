from uuid import uuid4

from app.domain.models.brewing_tools import BrewingTool
from app.domain.value_objects import BrewingToolID, ToolType


class BrewingToolService:
    def create_brewing_tool(
        self, name: str, tool_type: ToolType
    ) -> BrewingTool:
        return BrewingTool(
            id=BrewingToolID(uuid4()),
            name=name,
            type=tool_type,
            is_global=False,
        )
