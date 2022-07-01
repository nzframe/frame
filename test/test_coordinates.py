from utility.space_rect import XYCoordinate, SpaceRectangle
from model.direction import Orientation
import pytest


def test_XYCoordinate_init():
    assert XYCoordinate(1, 2).x == 1
    assert XYCoordinate(1, 2).y == 2

def test_XYCoordinate_change_value_x():
    cord = XYCoordinate(1, 2)
    cord = cord.move(x_delta = 1)
    assert cord == XYCoordinate(2, 2)

def test_XYCoordinate_change_value_y():
    cord = XYCoordinate(1, 2)
    cord = cord.move(y_delta = 1)
    assert cord == XYCoordinate(1, 3)

def test_XYCoordinate_tolist():
    assert XYCoordinate(1, 2).to_list() == [1, 2]
    

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

