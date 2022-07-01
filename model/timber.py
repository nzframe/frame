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

@total_ordering
class CuttedTimber(XYRectangle):
    class TimberTag(Enum):
        UNUSERD = auto()
        PLATE = auto()
        STUD = auto()

    def __init__(self, length, timber = Timber()) -> None:
        if length < 0:
            raise LengthLessThanZeroError()
        self.length: float = length
        self.timber: Timber = timber
        self.wall = None
        self.tag: Set[TimberType] = set()

    def purpose(self):
        class_path = str(self.__class__)
        return class_path.split("'")[1].split(".")[-1]

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

class Stud(CuttedTimber):
    orientation = Orientation.VERTICAL

    def __init__(self, length, timber=Timber()) -> None:
        super().__init__(length, timber)
        self.a_cord = XYCoordinate(0, 0)
        self.b_cord = XYCoordinate(self.timber.timber_size.height, 0)
        self.c_cord = XYCoordinate(self.timber.timber_size.height, self.length)
        self.d_cord = XYCoordinate(0, self.length)

class Plate(CuttedTimber):
    orientation = Orientation.HORIZONTAL

    def __init__(self, length, timber=Timber()) -> None:
        super().__init__(length, timber)
        self.a_cord = XYCoordinate(0, 0)
        self.b_cord = XYCoordinate(self.length, 0)
        self.c_cord = XYCoordinate(self.length, self.timber.timber_size.height)
        self.d_cord = XYCoordinate(0, self.timber.timber_size.height)

class TopPlate(Plate):
    position = Position.TOP
    
    def __init__(self, length, timber=Timber()) -> None:
        super().__init__(length, timber)
        

class BottomPlate(Plate):
    position = Position.BOTTOM

class LeftOuterStud(Stud):
    position = Position.LEFT

class RightOuterStud(Stud):
    position = Position.RIGHT
