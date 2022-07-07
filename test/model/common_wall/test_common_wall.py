from model.common import CommonWall, CommonWallComponents


def test_common_draw_it():
    common_wall = CommonWall(2330, 2310)
    from utility.draw import TestDraw
    from pathlib import Path
    file_path = Path(__file__).parent / "common_wall.png" 
    td = TestDraw(file_path.as_posix())
    
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
