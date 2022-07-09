from functools import total_ordering
from utility.space.rect import XYRectangle
from utility.space.cord import XYCoordinate
from model.direction import Orientation
from utility.space.line import XYLine
import copy


@total_ordering
class CuttedTimber(XYRectangle):
    """ cutted timber used to represent the materials used in door, window and retaining studs"""
    def __init__(self, length: float, orientation: Orientation):
        super().__init__()
        if length < 0:
            raise ValueError("The length of timber can't be negative")
        self.length: float = length
        self.orientation = orientation

        if self.orientation == Orientation.VERTICAL:
            self.a_cord = XYCoordinate(0, 0)
            self.b_cord = XYCoordinate(self.HEIGHT, 0)
            self.c_cord = XYCoordinate(self.HEIGHT, self.length)
            self.d_cord = XYCoordinate(0, self.length)

            ab_line: XYLine = XYLine(self.a_cord, self.b_cord)
            bc_line: XYLine = XYLine(self.b_cord, self.c_cord)
            cd_line: XYLine = XYLine(self.c_cord, self.d_cord)
            da_line: XYLine = XYLine(self.d_cord, self.a_cord)


        elif self.orientation == Orientation.HORIZONTAL:
            self.a_cord = XYCoordinate(0, 0)
            self.b_cord = XYCoordinate(self.length, 0)
            self.c_cord = XYCoordinate(self.length, self.HEIGHT)
            self.d_cord = XYCoordinate(0, self.HEIGHT) 

            ab_line: XYLine = XYLine(self.a_cord, self.b_cord)
            bc_line: XYLine = XYLine(self.b_cord, self.c_cord)
            cd_line: XYLine = XYLine(self.c_cord, self.d_cord)
            da_line: XYLine = XYLine(self.d_cord, self.a_cord)

    def __repr__(self) -> str:
        return super().__repr__()
    
    def __lt__(self, other):
        if not hasattr(self, "orientation") or not hasattr(other, "orientation"):
            raise ArithmeticError("Timber can't compare in this space")
        
        if self.orientation != other.orientation:
            raise ArithmeticError("Timber can't compare in this space")

        self_center: XYCoordinate = self.center()
        other_center: XYCoordinate = other.center()

        if self_center.x == other_center.x:
            return self.d_cord < other.a_cord
        elif self_center.y == other_center.y:
            return self.b_cord < other.a_cord

class Cutted2BY4(CuttedTimber):
    NAME: str = "TwoByFour"
    HEIGHT: float = 45
    WIDTH: float = 90

class CuttedLintel(CuttedTimber):
    NAME: str = "Lintel"
    HEIGHT: float = 240
    WIDTH: float = 90    

class CuttedHeader(CuttedTimber):
    NAME: str = "Header"
    HEIGHT: float = 90
    WIDTH: float = 90    

def distribute_timbers(begin_timber: CuttedTimber, end_timber: CuttedTimber, gap: float, is_blocker: bool = False):
    middle_timber = copy.copy(begin_timber)
    while True:
        if is_blocker:
            middle_timber.move_up(gap)
        elif begin_timber.orientation == Orientation.VERTICAL:
            middle_timber.move_right(gap)
        else:
            middle_timber.move_up(gap)


        if middle_timber < end_timber:
            yield middle_timber
        else:
            break

        middle_timber = copy.copy(middle_timber)
