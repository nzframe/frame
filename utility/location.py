from coordinates import spaced_coordinate
from dataclasses import dataclass

XYCoordinate = spaced_coordinate("XYCoordinate", "xy", ordered=True)

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