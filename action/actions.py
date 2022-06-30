from model.direction import Orientation
from model.wall import Wall
from model.timber import CuttedTimber, TopPlate, BottomPlate, LeftOuterStud, RightOuterStud, Timber


def add_top_plate(wall: Wall):
    timber = TopPlate(wall.wall_info.width)
    timber.wall = wall
    wall.register(timber)

def add_bottom_plate(wall: Wall):
    timber = BottomPlate(wall.wall_info.width)
    timber.wall = wall
    wall.register(timber)

def add_left_outer_stud(wall: Wall):
    timber = LeftOuterStud(wall.wall_info.height-Timber().timber_size.height*2)
    timber.wall = wall
    wall.register(timber)

def add_right_outer_stud(wall: Wall):
    timber = RightOuterStud(wall.wall_info.height-Timber().timber_size.height*2)
    timber.wall = wall
    wall.register(timber)

def move_timber(cutted_timber: CuttedTimber, value: int, orientation: Orientation):
    if orientation == Orientation.HORIZONTAL:
        pass
    elif orientation == Orientation.VERTICAL:
        pass

def create_wall(wall: Wall):
    add_top_plate(wall)
    add_bottom_plate(wall)
    add_left_outer_stud(wall)
    add_right_outer_stud(wall)
    return wall
