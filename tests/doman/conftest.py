import pytest

from app.adapters.password import PasswordHasher
from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.recipes import Recipe
from app.domain.models.users import User
from app.domain.services.brewing_tools import BrewingToolService
from app.domain.services.recipes import RecipeService
from app.domain.services.scoresheets import ScoresheetService
from app.domain.services.users import UserService
from app.domain.value_objects import (
    Coffee,
    ProcessingMethod,
    ToolType,
    WaterPouring,
)


@pytest.fixture
def tool_name() -> str:
    return 'Hario V60'


@pytest.fixture
def tool_type() -> ToolType:
    return ToolType.pour_over


@pytest.fixture
def brewing_tool_service() -> BrewingToolService:
    return BrewingToolService()


@pytest.fixture
def mock_brewing_tool(
    tool_name: str,
    tool_type: ToolType,
    brewing_tool_service: BrewingToolService,
) -> BrewingTool:
    return brewing_tool_service.create_brewing_tool(
        name=tool_name, tool_type=tool_type
    )


@pytest.fixture
def user_password() -> str:
    return 'some_password'


@pytest.fixture
def user_email() -> str:
    return 'some@example.com'


@pytest.fixture
def password_hasher() -> PasswordHasher:
    return PasswordHasher()


@pytest.fixture
def user_service(password_hasher: PasswordHasher) -> UserService:
    return UserService(password_hasher)


@pytest.fixture
def mock_user(
    user_service: UserService, user_email: str, user_password: str
) -> User:
    return user_service.create_user(email=user_email, password=user_password)


@pytest.fixture
def recipe_service() -> RecipeService:
    return RecipeService()


@pytest.fixture
def mock_recipe(
    mock_user: User,
    mock_brewing_tool: BrewingTool,
    recipe_service: RecipeService,
) -> Recipe:
    coffee = Coffee(
        name='Колумбия Уила',
        processing_method=ProcessingMethod.natural,
        region='Уила',
    )
    dose = 30
    grind = 32
    water_temperature = 92
    tools = [mock_brewing_tool]
    pours = [
        WaterPouring(45, 45),
        WaterPouring(45, 45),
        WaterPouring(45, 45),
        WaterPouring(45, 50),
        WaterPouring(45, 60),
    ]

    return recipe_service.create_recipe(
        user=mock_user,
        coffee=coffee,
        dose=dose,
        grind=grind,
        water_temperature=water_temperature,
        tools=tools,
        pours=pours,
    )


@pytest.fixture
def scoresheet_service() -> ScoresheetService:
    return ScoresheetService()
