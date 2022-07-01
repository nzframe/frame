from dataclasses import dataclass
from model.direction import Orientation, Position
from enum import Enum
from utility.space.rect import XYRectangle, XYCoordinate

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

class CuttedTimber(XYRectangle):
    def __init__(self, length, timber = Timber()) -> None:
        if length < 0:
            raise LengthLessThanZeroError()
        self.length: int = length
        self.timber: Timber = timber
        self.wall = None

    def purpose(self):
        class_path = str(self.__class__)
        return class_path.split("'")[1].split(".")[-1]

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
