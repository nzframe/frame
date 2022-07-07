from model.common import CommonWall
from utility.space.cord import XYCoordinate 


def test_generic_wall():
    cw = CommonWall(200, 200)
    cw.get_area()

    assert cw.area.a_cord == XYCoordinate(0, 0)
    assert cw.area.b_cord == XYCoordinate(200, 0)
    assert cw.area.c_cord == XYCoordinate(200, 290)
    assert cw.area.d_cord == XYCoordinate(0, 290)
