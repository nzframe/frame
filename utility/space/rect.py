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
    
    def move_up(self, value: int):
        self.a_cord = self.a_cord.move_up(value)
        self.b_cord = self.b_cord.move_up(value)
        self.c_cord = self.c_cord.move_up(value)
        self.d_cord = self.d_cord.move_up(value)

    def move_down(self, value: int):
        self.a_cord = self.a_cord.move_down(value)
        self.b_cord = self.b_cord.move_down(value)
        self.c_cord = self.c_cord.move_down(value)
        self.d_cord = self.d_cord.move_down(value)

    def move_right(self, value: int):
        self.a_cord = self.a_cord.move_right(value)
        self.b_cord = self.b_cord.move_right(value)
        self.c_cord = self.c_cord.move_right(value)
        self.d_cord = self.d_cord.move_right(value)
    
    def move_left(self, value: int):
        self.a_cord = self.a_cord.move_left(value)
        self.b_cord = self.b_cord.move_left(value)
        self.c_cord = self.c_cord.move_left(value)
        self.d_cord = self.d_cord.move_left(value)

    def move_a_to(self, target: XYCoordinate):
        self.__move_rect_overlap_x_with__(self.a_cord, target)

    def move_b_to(self, target: XYCoordinate):
        self.__move_rect_overlap_x_with__(self.b_cord, target)

    def move_c_to(self, target: XYCoordinate):
        self.__move_rect_overlap_x_with__(self.c_cord, target)

    def move_d_to(self, target: XYCoordinate):
        self.__move_rect_overlap_x_with__(self.d_cord, target)

    def __move_rect_overlap_x_with__(self, based_on_cord: XYCoordinate, target: XYCoordinate):
        distanct = target - based_on_cord 
        
        new = self.a_cord + distanct
        self.a_cord = XYCoordinate(new.x, new.y)

        new = self.b_cord + distanct
        self.b_cord = XYCoordinate(new.x, new.y)       

        new = self.c_cord + distanct
        self.c_cord = XYCoordinate(new.x, new.y)   

        new = self.d_cord + distanct
        self.d_cord = XYCoordinate(new.x, new.y)           