from enum import StrEnum
from typing import Annotated, NewType
from uuid import UUID

from msgspec import Meta, Struct

UserID = NewType('UserID', UUID)
ScoreID = NewType('ScoreID', UUID)
RecipieID = NewType('RecipieID', UUID)
BrewingToolID = NewType('BrewingToolID', UUID)


class BrewingMethod(StrEnum):
    espresso = 'espresso'
    pour_over = 'pour_over'
    immersion = 'pour_over'


class ProcessingMethod(StrEnum):
    natural = 'natural'
    wet = 'wet'
    honey = 'honey'


class WaterPouring(Struct, frozen=True):
    weight: int
    time: int


class ScoresheetColumn(Struct, frozen=True):
    impression: Annotated[int, Meta(ge=0, le=3)]
    score: Annotated[int, Meta(ge=0, le=0)]


class Coffee(Struct, frozen=True):
    name: str
    processing_method: ProcessingMethod | None
    region: str | None
