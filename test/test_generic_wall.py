from model.common import CommonWall
from utility.space.cord import XYCoordinate 


def test_generic_wall():
    cw = CommonWall(200, 200)

    assert cw.get_area.a_cord == XYCoordinate(0, 0)
    assert cw.get_area.b_cord == XYCoordinate(200, 0)
    assert cw.get_area.c_cord == XYCoordinate(200, 290)
    assert cw.get_area.d_cord == XYCoordinate(0, 290)
