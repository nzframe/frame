from cmath import log
from utility.space.rect import XYCoordinate
import pytest


def test_XYCoordinate_init():
    assert XYCoordinate(1, 2).x == 1
    assert XYCoordinate(1, 2).y == 2

def test_XYCoordinate_change_value_x():
    cord = XYCoordinate(1, 2)
    cord = cord.move_right(1)
    assert cord == XYCoordinate(2, 2)

def test_XYCoordinate_change_value_y():
    cord = XYCoordinate(1, 2)
    cord = cord.move_up(1)
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

def test_XYCoordinate_compare_x_axis():
    a = XYCoordinate(1, 3)
    b = XYCoordinate(2, 3)    
    assert a < b

def test_XYCoordinate_compare_y_axis():
    a = XYCoordinate(1, 2)
    b = XYCoordinate(1, 3)    
    assert a < b

def test_XYCoordinate_compare_arithmeticError():
    with pytest.raises(ArithmeticError):
        a = XYCoordinate(1, 2)
        b = XYCoordinate(3, 3)    
        a < b

def test_XYCoordinate_repr():
    a = XYCoordinate(1, 2)
    assert a.__repr__() == "XYCoordinate({'x': 1, 'y': 2})"
