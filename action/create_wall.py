from model.wall import Wall
from model.timber import BottomPlate, LeftOuterStud, RightOuterStud, TopPlate, Timber


def create_wall(wall: Wall):
    wall.register(TopPlate(wall.wall_info.width))
    wall.register(BottomPlate(wall.wall_info.width))
    wall.register(LeftOuterStud(wall.wall_info.height-Timber().timber_size.height*2))
    wall.register(RightOuterStud(wall.wall_info.height-Timber().timber_size.height*2))
    return wall
