from app.domain.models.brewing_tools import BrewingTool
from app.domain.services.brewing_tools import BrewingToolService
from app.domain.value_objects import ToolType


def test_create_brewing_tool(
    tool_name: str,
    tool_type: ToolType,
    brewing_tool_service: BrewingToolService,
) -> None:
    tool = brewing_tool_service.create_brewing_tool(
        name=tool_name, tool_type=tool_type
    )

    assert tool.name == tool_name
    assert tool.type == tool_type


def test_making_tool_global(mock_brewing_tool: BrewingTool) -> None:
    mock_brewing_tool.make_global()

    assert mock_brewing_tool.is_global is True
