import pytest
from model.timber import Cutted2BY4
from model.direction import Orientation
from utility.space.cord import XYCoordinate


def test_cutted_timber_default_value():
    door_width = 1830
    timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
    assert timber.a_cord == XYCoordinate(0, 0)
    assert timber.b_cord == XYCoordinate(2010, 0)
    assert timber.c_cord == XYCoordinate(2010, 45)
    assert timber.d_cord == XYCoordinate(0, 45)

    timber.move_up(45)

    assert timber.a_cord == XYCoordinate(0, 45)

def test_cutted_timber_less_compare():
    bottom_blocker = Cutted2BY4(250, Orientation.VERTICAL)
    top_blocker = Cutted2BY4(250, Orientation.VERTICAL)
    top_blocker.move_up(100)

    bottom_blocker.move_up(200)
    assert top_blocker.a_cord < bottom_blocker.a_cord 

