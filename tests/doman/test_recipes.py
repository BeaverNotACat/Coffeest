from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.users import User
from app.domain.services.recipes import RecipeService
from app.domain.value_objects import Coffee, WaterPouring


def test_recipe_creation(recipe_service: RecipeService, mock_user: User, mock_brewing_tool: BrewingTool) -> None:
    coffee = Coffee(name="Нескафе 3 в 1")
    water_temperature = 92
    brewing_tools = [mock_brewing_tool]
    pours = [
        WaterPouring(100, 60),
        WaterPouring(250, 30),
    ]
    total_time = 90
    
    recipe = recipe_service.create_recipe(
        user=mock_user,
        coffee=coffee,
        water_temperature=water_temperature,
        brewing_tools=brewing_tools,
        pours=pours
    )

    assert recipe.user == mock_user.id
    assert recipe.coffee == coffee
    assert recipe.water_temperature == water_temperature
    assert recipe.brewing_tools == brewing_tools
    assert recipe.pours == pours
    assert recipe.total_time == total_time
