from typing import Annotated
from uuid import uuid4

from annotated_types import MinLen

from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.recipes import Recipe
from app.domain.models.users import User
from app.domain.value_objects import Coffee, RecipieID, WaterPouring


class RecipeService:
    def create_recipe(
        self,
        user: User,
        coffee: Coffee,
        dose: float,
        grind: float,
        water_temperature: int,
        tools: Annotated[list[BrewingTool], MinLen(1)],
        pours: Annotated[list[WaterPouring], MinLen(1)],
    ) -> Recipe:
        return Recipe(
            id=RecipieID(uuid4()),
            author=user.id,
            coffee=coffee,
            dose=dose,
            grind=grind,
            water_temperature=water_temperature,
            tools=tools,
            pours=pours,
        )
