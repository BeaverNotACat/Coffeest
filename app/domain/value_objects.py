from enum import StrEnum
from typing import Annotated, NewType
from uuid import UUID

from msgspec import Meta, Struct

UserID = NewType('UserID', UUID)
ScoreID = NewType('ScoreID', UUID)
RecipieID = NewType('RecipieID', UUID)
BrewingToolID = NewType('BrewingToolID', UUID)


class ToolType(StrEnum):
    espresso = 'espresso'
    pour_over = 'pour_over'
    immersion = 'pour_over'


class ProcessingMethod(StrEnum):
    natural = 'natural'
    honey = 'honey'
    wet = 'wet'
    wet_hulled = 'wet_hulled'


class WaterPouring(Struct, frozen=True):
    weight: int
    time: int


class ScoresheetColumn(Struct, frozen=True):
    impression: Annotated[int, Meta(ge=0, le=3)]
    score: Annotated[int, Meta(ge=0, le=9)]


class Coffee(Struct, frozen=True):
    name: str
    processing_method: ProcessingMethod | None = None
    region: str | None = None
