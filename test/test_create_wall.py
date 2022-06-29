from operator import le
import pytest
from model.wall import Wall, WallInfo
from action.create_wall import create_wall
from model.timber import TopPlate, BottomPlate, LeftOuterStud, RightOuterStud


def test_create_wall():
    wall = create_wall(Wall(WallInfo(2400, 2550)))
    assert wall.get_total_timbers() == 4
    
    top_plate: TopPlate =  wall.topplate
    assert top_plate.length == 2400

    bottom_plate: BottomPlate = wall.bottomplate
    assert bottom_plate.length == 2400

    left_outer_stud: LeftOuterStud = wall.leftouterstud
    assert left_outer_stud.length == 2460

    right_outer_stud: RightOuterStud = wall.rightouterstud
    assert right_outer_stud.length == 2460
