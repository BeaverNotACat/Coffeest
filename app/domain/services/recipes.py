from typing import Annotated
from uuid import uuid4

from annotated_types import MinLen

from app.domain.models.brewing_tools import BrewingTool
from app.domain.models.recipes import Recipie
from app.domain.models.users import User
from app.domain.value_objects import Coffee, RecipieID, WaterPouring


class RecipeService:
    def create_recipe(
        self,
        user: User,
        coffee: Coffee,
        water_temperature: int,
        brewing_tools: Annotated[list[BrewingTool], MinLen(1)],
        pours: Annotated[list[WaterPouring], MinLen(1)],
    ) -> Recipie:
        return Recipie(
            id=RecipieID(uuid4()),
            user=user.id,
            coffee=coffee,
            water_temperature=water_temperature,
            brewing_tools=brewing_tools,
            pours=pours,
        )
