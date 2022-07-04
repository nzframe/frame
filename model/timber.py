from functools import total_ordering
from utility.space.rect import XYRectangle
from utility.space.cord import XYCoordinate
from model.direction import Orientation
from utility.space.line import XYLine

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


class Cutted2BY4(CuttedTimber):
    NAME: str = "TwoByFour"
    HEIGHT: float = 45
    WIDTH: float = 90

class CuttedHeader(CuttedTimber):
    NAME: str = "Header"
    HEIGHT: float = 240
    WIDTH: float = 90    