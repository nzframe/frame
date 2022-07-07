from model.load_point import LoadPoint, LoadPointComponents
from utility.draw.draw_load_point import draw_load_point

def test_draw_load_point():
    load_point = LoadPoint(2310, 5)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "load_point.png" 
    td = DrawIT(file_path.as_posix())

    draw_load_point(td, load_point)

def test_python_range():
    assert [i for i in range(1, 4)] == [1, 2, 3]