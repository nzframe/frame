from model.direction import Orientation
from model.wall import Wall
from model.timber import CuttedTimber, TopPlate, BottomPlate, LeftOuterStud, RightOuterStud, Timber


def add_top_plate(wall: Wall):
    timber = TopPlate(wall.wall_info.width)
    timber.move_up((wall.d_cord - timber.d_cord).norm())
    timber.wall = wall
    wall.register(timber)
    return wall

def add_bottom_plate(wall: Wall):
    timber = BottomPlate(wall.wall_info.width)
    timber.wall = wall
    wall.register(timber)
    return wall

def add_left_outer_stud(wall: Wall):
    timber = LeftOuterStud(wall.wall_info.height-Timber().timber_size.height*2)
    bottom_plate: BottomPlate = wall.bottom_plate
    timber.move_up(bottom_plate.timber.timber_size.height)
    timber.wall = wall
    wall.register(timber)
    return wall

def add_right_outer_stud(wall: Wall):
    timber = RightOuterStud(wall.wall_info.height-Timber().timber_size.height*2)
    bottom_plate: BottomPlate = wall.bottom_plate
    timber.move_right((wall.b_cord - timber.b_cord).norm())
    timber.move_up(bottom_plate.timber.timber_size.height)
    timber.wall = wall
    wall.register(timber)
    return wall

def create_wall(wall: Wall):
    add_top_plate(wall)
    add_bottom_plate(wall)
    add_left_outer_stud(wall)
    add_right_outer_stud(wall)
    return wall
