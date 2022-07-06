import pytest
from utility.space.cord import XYCoordinate
from utility.space.rect import XYRectangle

def test_rect_center():
    s = XYRectangle(
        XYCoordinate(1,1),
        XYCoordinate(3,1),
        XYCoordinate(3,3),
        XYCoordinate(1,3)
        )
    assert s.center() == XYCoordinate(2, 2)

def test_center_to_center_distance():
    s = XYRectangle(
        XYCoordinate(1,1),
        XYCoordinate(3,1),
        XYCoordinate(3,3),
        XYCoordinate(1,3)
        )

    d = XYRectangle(
        XYCoordinate(3,1),
        XYCoordinate(5,1),
        XYCoordinate(5,3),
        XYCoordinate(3,3)
        )

    assert s - d == 2

def test_rect_move_based_on_cord():
    rect = XYRectangle(XYCoordinate(0, 0), XYCoordinate(1, 0), XYCoordinate(1, 1), XYCoordinate(0, 1))
    rect.move_a_to(XYCoordinate(1, 1))
    assert rect.a_cord == XYCoordinate(1, 1)
    assert rect.b_cord == XYCoordinate(2, 1)
    assert rect.c_cord == XYCoordinate(2, 2)
    assert rect.d_cord == XYCoordinate(1, 2)