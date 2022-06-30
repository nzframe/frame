from operator import le
import pytest
from model.wall import Wall, WallInfo
from action.actions import create_wall
from model.timber import TopPlate, BottomPlate, LeftOuterStud, RightOuterStud


def test_create_wall():
    wall = create_wall(Wall(WallInfo(2400, 2550)))
    assert wall.get_total_timbers() == 4
    
    assert wall.top_plate.length == 2400

    assert wall.bottom_plate.length == 2400

    assert wall.left_outer_stud.length == 2460

    assert wall.right_outer_stud.length == 2460
