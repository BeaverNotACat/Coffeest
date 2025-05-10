from uuid import uuid4

import pytest

from app.domain.exceptions.scoresheets import SetScoreToForegnRecipieError
from app.domain.models.recipes import Recipe
from app.domain.models.users import User
from app.domain.services.scoresheets import ScoresheetService
from app.domain.value_objects import ScoresheetColumn, UserID


def test_create_scoresheet(
    scoresheet_service: ScoresheetService,
    mock_user: User,
    mock_recipe: Recipe,
) -> None:
    aroma = ScoresheetColumn(3, 8)
    flavor = ScoresheetColumn(3, 8)
    aftertaste = ScoresheetColumn(3, 8)
    acidity = ScoresheetColumn(3, 9)
    sweetness = ScoresheetColumn(3, 9)
    mouthfeel = ScoresheetColumn(3, 9)
    overall_score = (8 * 3 + 9 * 3) / 6

    scoresheet = scoresheet_service.create_scoresheet(
        user=mock_user,
        recipe=mock_recipe,
        aroma=aroma,
        flavor=flavor,
        aftertaste=aftertaste,
        acidity=acidity,
        sweetness=sweetness,
        mouthfeel=mouthfeel,
    )

    assert scoresheet.recipie == mock_recipe.id
    assert scoresheet.author == mock_user.id
    assert scoresheet.aroma == aroma
    assert scoresheet.flavor == flavor
    assert scoresheet.flavor == flavor
    assert scoresheet.aftertaste == aftertaste
    assert scoresheet.acidity == acidity
    assert scoresheet.sweetness == sweetness
    assert scoresheet.mouthfeel == mouthfeel
    assert scoresheet.overall == overall_score


def test_only_recipe_author_can_add_scoresheet(
    scoresheet_service: ScoresheetService,
    mock_user: User,
    mock_recipe: Recipe,
) -> None:
    mock_user.id = UserID(uuid4())

    with pytest.raises(SetScoreToForegnRecipieError):
        scoresheet_service.create_scoresheet(
            user=mock_user,
            recipe=mock_recipe,
            aroma=ScoresheetColumn(3, 9),
            flavor=ScoresheetColumn(3, 9),
            aftertaste=ScoresheetColumn(3, 9),
            acidity=ScoresheetColumn(3, 9),
            sweetness=ScoresheetColumn(3, 9),
            mouthfeel=ScoresheetColumn(3, 9),
        )
