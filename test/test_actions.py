from operator import le
import pytest
from model.wall import Wall, WallInfo
from action.actions import create_wall, add_top_plate
from model.timber import TopPlate, Plate
from utility.location import XYCoordinate


def test_create_wall():
    wall = create_wall(Wall(WallInfo(2400, 2550)))
    assert wall.get_total_timbers() == 4
    assert wall.top_plate.length == 2400
    assert wall.bottom_plate.length == 2400
    assert wall.left_outer_stud.length == 2460
    assert wall.right_outer_stud.length == 2460

def test_type_of_cutted_timber():
    top_plate = TopPlate(1330)
    assert top_plate.__class__.__name__ == "TopPlate" 

def test_move_up_timber():
    timber = Plate(1330)
    timber.move_up(70)
    assert timber.a_cord == XYCoordinate(0, 70)

def test_move_down_timber():
    timber = Plate(1330)
    timber.move_down(30)
    assert timber.a_cord == XYCoordinate(0, -30)

def test_move_left_timber():
    timber = Plate(1330)
    timber.move_left(30)
    assert timber.a_cord == XYCoordinate(-30, 0)

def test_move_right_timber():
    timber = Plate(1330)
    timber.move_right(30)
    assert timber.a_cord == XYCoordinate(30, 0)

def test_add_top_plate():
    wall: Wall = create_wall(Wall(WallInfo(440, 330)))
    wall = add_top_plate(wall)
    top_plate: TopPlate = wall.top_plate
    assert top_plate.a_cord == XYCoordinate(0, 285)

def test_wall_cord():
    wall: Wall = create_wall(Wall(WallInfo(440, 330)))
    assert wall.c_cord == XYCoordinate(440, 330)

def test_wall_cord_minus_timber_cord():
    wall: Wall = create_wall(Wall(WallInfo(440, 330)))
    plate: Plate = Plate(200)
    assert (wall.b_cord - plate.b_cord).norm() == 240