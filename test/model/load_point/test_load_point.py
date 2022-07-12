from model.load_point import LoadPoint
from utility.draw.draw_for_test import draw_component

def test_draw_load_point():
    load_point = LoadPoint(2310, 5)
    load_point.group()
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "load_point.png" 
    td = DrawIT(file_path.as_posix())

    draw_component(td, load_point)

def test_python_range():
    assert [i for i in range(1, 4)] == [1, 2, 3]

def test_draw_load_point_move_right():
    load_point = LoadPoint(2310, 5)
    load_point.group()
    load_point.move_right(300)
    load_point.bottom_plate.move_right(300)
    load_point.top_plate.move_right(300)    
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "load_point_move_right.png" 
    td = DrawIT(file_path.as_posix())


    draw_component(td, load_point)