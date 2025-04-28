from uuid import uuid4

from app.domain.exceptions.scoresheets import SetScoreToForegnRecipieError
from app.domain.models.recipes import Recipie
from app.domain.models.scoresheets import Scoresheet
from app.domain.models.users import User
from app.domain.value_objects import ScoreID, ScoresheetColumn


class ScoresheetService:
    def create_scoresheet(
        self,
        user: User,
        recipie: Recipie,
        aroma: ScoresheetColumn,
        flavor: ScoresheetColumn,
        aftertaste: ScoresheetColumn,
        acidity: ScoresheetColumn,
        sweetness: ScoresheetColumn,
        mouthfeel: ScoresheetColumn,
    ) -> Scoresheet:
        if user.id != recipie.user:
            raise SetScoreToForegnRecipieError

        return Scoresheet(
            id=ScoreID(uuid4()),
            user=user.id,
            recipie=recipie.id,
            aroma=aroma,
            flavor=flavor,
            aftertaste=aftertaste,
            acidity=acidity,
            sweetness=sweetness,
            mouthfeel=mouthfeel,
        )
