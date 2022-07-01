import pytest
from utility.space.cord import XYCoordinate
from utility.space.rect import XYRectangle

def test_space_rectangle_center():
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