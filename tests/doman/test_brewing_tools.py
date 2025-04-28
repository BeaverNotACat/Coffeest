from app.domain.models.brewing_tools import BrewingTool
from app.domain.services.brewing_tools import BrewingToolService
from app.domain.value_objects import BrewingMethod

def test_create_brewing_tool(
    tool_name: str,
    tool_method: BrewingMethod,
    brewing_tool_service: BrewingToolService,
) -> None:
    tool = brewing_tool_service.create_brewing_tool(name=tool_name, method=tool_method)

    assert tool.name == tool_name
    assert tool.method == tool_method


def test_making_tool_global(mock_brewing_tool: BrewingTool) -> None:
    mock_brewing_tool.make_global()

    assert mock_brewing_tool.is_global is True
