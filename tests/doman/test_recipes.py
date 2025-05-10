from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.users import User
from app.domain.services.recipes import RecipeService
from app.domain.value_objects import Coffee, ProcessingMethod, WaterPouring


def test_recipe_creation(
    recipe_service: RecipeService,
    mock_user: User,
    mock_brewing_tool: BrewingTool,
) -> None:
    coffee = Coffee(
        name='Колумбия Уила',
        processing_method=ProcessingMethod.natural,
        region='Уила',
    )
    dose = 30
    grind = 32
    water_temperature = 92
    tools: list[BrewingTool] = []
    pours = [
        WaterPouring(45, 45),
        WaterPouring(45, 45),
        WaterPouring(45, 45),
        WaterPouring(45, 50),
        WaterPouring(45, 60),
    ]
    total_time = 45 * 3 + 50 + 60
    total_water = 45 * 5

    recipe = recipe_service.create_recipe(
        user=mock_user,
        coffee=coffee,
        dose=dose,
        grind=grind,
        water_temperature=water_temperature,
        tools=tools,
        pours=pours,
    )

    assert recipe.author == mock_user.id
    assert recipe.coffee == coffee
    assert recipe.water_temperature == water_temperature
    assert recipe.tools == tools
    assert recipe.pours == pours
    assert recipe.total_time == total_time
    assert recipe.total_water == total_water
