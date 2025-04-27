import pytest

from app.domain.models.brewing_tools import BrewingTool
from app.domain.services.brewing_tools import BrewingToolService
from app.domain.value_objects import BrewingMethod


@pytest.fixture
def brewing_tool_name() -> str:
    return 'Hario V60'


@pytest.fixture
def brewing_tool_method() -> BrewingMethod:
    return BrewingMethod.pour_over


@pytest.fixture
def brewing_tool_service() -> BrewingToolService:
    return BrewingToolService()


@pytest.fixture
def brewing_tool(
    brewing_tool_name: str,
    brewing_tool_method: BrewingMethod,
    brewing_tool_service: BrewingToolService,
) -> BrewingTool:
    return brewing_tool_service.create_brewing_tool(
        name=brewing_tool_name, method=brewing_tool_method
    )


def test_create_brewing_tool(
    brewing_tool_name: str,
    brewing_tool_method: BrewingMethod,
    brewing_tool_service: BrewingToolService,
) -> None:
    tool = brewing_tool_service.create_brewing_tool(
        name=brewing_tool_name, method=brewing_tool_method
    )

    assert tool.name == brewing_tool_name
    assert tool.method == brewing_tool_method


def test_making_tool_global(brewing_tool: BrewingTool) -> None:
    brewing_tool.make_global()

    assert brewing_tool.is_global is True
