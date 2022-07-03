from dataclasses import dataclass
from enum import Enum, auto
from functools import total_ordering
from typing import Set

from utility.space.rect import XYCoordinate, XYRectangle

from model.direction import Orientation, Position


class LengthLessThanZeroError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TimberType(Enum):
    TWOBYFOURS = 1

@dataclass
class TimberSize:
    height: float
    width: float

class Timber:
    timber_type: TimberType = TimberType.TWOBYFOURS
    timber_size: TimberSize = TimberSize(45, 90)

class TimberTag(Enum):
    UNUSERD = auto()
    USED = auto()

@total_ordering
class CuttedTimber(XYRectangle):
    """ cutted timber used to represent the materials used in door, window and retaining studs"""
    def __init__(self, length, timber = Timber()) -> None:
        if length < 0:
            raise LengthLessThanZeroError()
        self.length: float = length
        self.timber: Timber = timber
        self.wall = None
        self.tag: Set[TimberType] = set()

    def __lt__(self, other):
        if hasattr(self, "orientation") and hasattr(other, "orientation") and self.orientation == other.orientation:
            if self.orientation == Orientation.VERTICAL:
                return self.a_cord.x < other.a_cord.x
            else:
                return self.a_cord.y < other.a_cord.y
        else:
            raise Exception("Timber can't compare in this space")
    
    def __eq__(self, other):
        if hasattr(self, "orientation") and hasattr(other, "orientation") and self.orientation == other.orientation:
            if self.orientation == Orientation.VERTICAL:
                return self.a_cord.x == other.a_cord.x
            else:
                return self.a_cord.y == other.a_cord.y
        else:
            raise Exception("Timber can't compare in this space")       
