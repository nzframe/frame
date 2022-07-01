from dataclasses import dataclass
from model.direction import Orientation
from utility.space.cord import XYCoordinate
from utility.space.line import XYLine

@dataclass
class XYRectangle:
    a_cord: XYCoordinate = None
    b_cord: XYCoordinate = None
    c_cord: XYCoordinate = None
    d_cord: XYCoordinate = None

    ab_line: XYLine = None if a_cord is None and b_cord is None else XYLine(a_cord, b_cord)
    bc_line: XYLine = None if b_cord is None and c_cord is None else XYLine(b_cord, c_cord)
    cd_line: XYLine = None if c_cord is None and d_cord is None else XYLine(c_cord, d_cord)
    da_line: XYLine = None if d_cord is None and a_cord is None else XYLine(d_cord, a_cord)

    def center(self) -> XYCoordinate: 
        """get the gravity point of the rectangle

        Returns:
            XYCoordinate: the coordinate of gravity point 
        """
        return XYCoordinate((self.a_cord.x + self.c_cord.x)/2, (self.a_cord.y + self.c_cord.y)/2)
            
    def __sub__(self, other) -> int:
        return (self.center() - other.center()).norm()

    def __move__(self, value: int, orientation: Orientation):
        if orientation == Orientation.VERTICAL:
            self.a_cord = self.a_cord.move(y_delta = value)
            self.b_cord = self.b_cord.move(y_delta = value)
            self.c_cord = self.c_cord.move(y_delta = value)
            self.d_cord = self.d_cord.move(y_delta = value)
        elif orientation == Orientation.HORIZONTAL:
            self.a_cord = self.a_cord.move(x_delta = value)
            self.b_cord = self.b_cord.move(x_delta = value)
            self.c_cord = self.c_cord.move(x_delta = value)
            self.d_cord = self.d_cord.move(x_delta = value)
    
    def move_up(self, value: int):
        self.__move__(value, Orientation.VERTICAL)

    def move_down(self, value: int):
        self.__move__(value * -1, Orientation.VERTICAL)

    def move_right(self, value: int):
        self.__move__(value, Orientation.HORIZONTAL)
    
    def move_left(self, value: int):
        self.__move__(value * -1, Orientation.HORIZONTAL)
