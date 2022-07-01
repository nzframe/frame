from sympy import Point, Line 
from utility.space.cord import XYCoordinate

class XYLine():
    def __init__(self, point_a: XYCoordinate, point_b: XYCoordinate) -> None:
        sympy_point_a = Point(point_a.x, point_a.y)
        sympy_point_b = Point(point_b.x, point_b.y)
        self.line = Line(sympy_point_a, sympy_point_b)

    def distance(self, cord: XYCoordinate):
        """ get a distance to a XYCord """
        sympy_point = Point(cord.x, cord.y)
        return self.line.distance(sympy_point)
