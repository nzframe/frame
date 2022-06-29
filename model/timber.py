from dataclasses import dataclass
from model.direction import Orientation, Position
from enum import Enum

class LengthLessThanZeroError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TimberType(Enum):
    TWOBYFOURS = 1

@dataclass
class TimberSize:
    height: int
    width: int

class Timber:
    timber_type: TimberType = TimberType.TWOBYFOURS
    timber_size: TimberSize = TimberSize(45, 90)

class CuttedTimber:
    def __init__(self, length, timber = Timber()) -> None:
        if length < 0:
            raise LengthLessThanZeroError()
        self.length = length
        self.timber = timber
        self.a_cord = None
        self.b_cord = None
        self.c_cord = None
        self.d_cord = None

    def purpose(self):
        class_path = str(self.__class__)
        return class_path.split("'")[1].split(".")[-1]

class Stud(CuttedTimber):
    orientation = Orientation.VERTICAL

class Plate(CuttedTimber):
    orientation = Orientation.HORIZONTAL

class TopPlate(Plate):
    position = Position.TOP

class BottomPlate(Plate):
    position = Position.BOTTOM

class LeftOuterStud(Stud):
    position = Position.LEFT

class RightOuterStud(Stud):
    position = Position.RIGHT
