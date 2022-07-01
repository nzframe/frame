import pytest
from utility.coordinates import XYCoordinate
from utility.space_rect import SpaceRectangle

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