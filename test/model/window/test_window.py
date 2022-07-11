from model.window import Window
from utility.draw.draw_window import draw_window
import pytest 


def test_draw_window_door():
    window = Window(2170, 1095, 1300, 2630)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "window_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_window(td, window)
    
def test_pairwise():
    from more_itertools import pairwise
    a = [1,2,3]
    assert [(x, y) for x, y in pairwise(a)] == [(1, 2), (2, 3)]

def test_draw_window_door_move_right():
    window = Window(2170, 1095, 630, 2630)
    window.move_right(300)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "window_door_move_right.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_window(td, window)

def test_draw_window_door_init_exception():
    with pytest.raises(ValueError):
        window = Window(2170, 1095, 90, 2630)