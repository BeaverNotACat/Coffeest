from msgspec import Struct

from app.domain.value_objects import (
    RecipieID,
    ScoreID,
    ScoresheetColumn,
    UserID,
)


class Scoresheet(Struct):
    id: ScoreID
    user: UserID
    recipie: RecipieID

    aroma: ScoresheetColumn
    flavor: ScoresheetColumn
    aftertaste: ScoresheetColumn
    acidity: ScoresheetColumn
    sweetness: ScoresheetColumn
    mouthfeel: ScoresheetColumn

    @property
    def overall(self) -> float:
        return (
            self.aroma.score
            + self.flavor.score
            + self.aftertaste.score
            + self.acidity.score
            + self.sweetness.score
            + self.mouthfeel.score
        ) / 6
