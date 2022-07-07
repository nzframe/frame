from model.common import CommonWall


def test_common_draw_it():
    common_wall = CommonWall(800, 2310)
    from utility.draw import TestDraw
    from pathlib import Path
    file_path = Path(__file__).parent / "common_wall.png" 
    td = TestDraw(file_path.as_posix())
    
    common_wall_cpnt: CommonWall = common_wall.components
    td.prepare(common_wall.top_plate)
    td.prepare(common_wall.bottom_plate)
    td.prepare(common_wall.left_king_stud)
    td.prepare(common_wall.right_king_stud)

    for cripple in common_wall.components:
        td.prepare(cripple)

    td.draw_it()
