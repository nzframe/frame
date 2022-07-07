from utility.draw import DrawIT
from model.common import CommonWall, CommonWallComponents


def draw_common_wall(td: DrawIT, common_wall: CommonWall):    
    common_wall_cpnt: CommonWallComponents = common_wall.components
    td.prepare(common_wall.top_plate)
    td.prepare(common_wall.bottom_plate)
    td.prepare(common_wall.left_king_stud)
    td.prepare(common_wall.right_king_stud)

    for stud in common_wall_cpnt.studs:
        td.prepare(stud)

    for nogging in common_wall.noggings:
        td.prepare(nogging)
    td.draw_it()
