import imp
from model.wall import Wall
from model.timber import TopPlate, BottomPlate, LeftOuterStud, RightOuterStud, Timber


def add_top_plate(wall: Wall):
    wall.register(TopPlate(wall.wall_info.width))

def add_bottom_plate(wall: Wall):
    wall.register(BottomPlate(wall.wall_info.width))

def add_left_outer_stud(wall: Wall):
    wall.register(LeftOuterStud(wall.wall_info.height-Timber().timber_size.height*2))

def add_right_outer_stud(wall: Wall):
    wall.register(RightOuterStud(wall.wall_info.height-Timber().timber_size.height*2))

def create_wall(wall: Wall):
    add_top_plate(wall)
    add_bottom_plate(wall)
    add_left_outer_stud(wall)
    add_right_outer_stud(wall)
    return wall
