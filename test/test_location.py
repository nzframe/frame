from utility.location import XYCoordinate, SpaceRectangle
from model.direction import Orientation
import pytest


def test_XYCoordinate():
    assert XYCoordinate(1, 2).x == 1
    assert XYCoordinate(1, 2).y == 2

def test_XYCoordinate_property_exception():
    with pytest.raises(AttributeError):
        XYCoordinate(1,2).z

def test_XYCoordinate_substract():
    a = XYCoordinate(1, 2)
    b = XYCoordinate(1, 3)
    c = XYCoordinate(4, 2)
    assert a - b == XYCoordinate(0, -1)
    assert c - a == XYCoordinate(3, 0)

def test_XYCoordinate_add():
    a = XYCoordinate(1, 2)
    b = XYCoordinate(1, 3)
    c = XYCoordinate(4, 2)
    assert a + b == XYCoordinate(2, 5)
    assert c + a == XYCoordinate(5, 4)

def test_space_rectangle_center():
    s = SpaceRectangle(
        XYCoordinate(1,1),
        XYCoordinate(3,1),
        XYCoordinate(3,3),
        XYCoordinate(1,3)
        )
    assert s.center() == XYCoordinate(2, 2)

def test_center_to_center_distance():
    s = SpaceRectangle(
        XYCoordinate(1,1),
        XYCoordinate(3,1),
        XYCoordinate(3,3),
        XYCoordinate(1,3)
        )

    d = SpaceRectangle(
        XYCoordinate(3,1),
        XYCoordinate(5,1),
        XYCoordinate(5,3),
        XYCoordinate(3,3)
        )

    assert s - d == 2