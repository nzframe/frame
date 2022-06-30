from coordinates import spaced_coordinate
from dataclasses import dataclass
from model.direction import Orientation
import logging

XYCoordinate = spaced_coordinate("XYCoordinate", "xy", ordered=True)

def move(self, x_delta: int = 0, y_delta: int = 0):
    return XYCoordinate(self.x + x_delta, self.y + y_delta)

setattr(XYCoordinate, "move", move)

@dataclass
class SpaceRectangle:
    a_cord: XYCoordinate = None
    b_cord: XYCoordinate = None
    c_cord: XYCoordinate = None
    d_cord: XYCoordinate = None

    def center(self) -> XYCoordinate: 
        """get the gravity point of the rectangle

        Returns:
            XYCoordinate: the coordinate of gravity point 
        """
        return XYCoordinate((self.a_cord.x + self.c_cord.x)/2, (self.a_cord.y + self.c_cord.y)/2)
            
    def __sub__(self, other) -> int:
        return (self.center() - other.center()).norm()

    def move(self, value: int, orientation: Orientation):
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
        self.move(value, Orientation.VERTICAL)

    def move_down(self, value: int):
        self.move(value * -1, Orientation.VERTICAL)

    def move_right(self, value: int):
        self.move(value, Orientation.HORIZONTAL)
    
    def move_left(self, value: int):
        self.move(value * -1, Orientation.HORIZONTAL)