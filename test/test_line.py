from utility.space.line import XYLine
from utility.space.cord import XYCoordinate


def test_cord_line_distance():
    a = XYCoordinate(1, 2)
    b = XYCoordinate(3, 2)
    c = XYCoordinate(0, 0)

    line = XYLine(a, b)
    assert line.distance(c) == 2