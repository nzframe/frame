from multiprocessing.sharedctypes import Value
from model.door import HeaderDoor, HeaderDoorComponents
from utility.draw.draw_header_door import draw_header_door
import pytest 


def test_draw_header_door():
    door = HeaderDoor(930, 2170, 2630)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "header_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_header_door(td, door)

def test_draw_header_door_move_right():
    door = HeaderDoor(930, 2170, 2630)
    door.move_right(300)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "header_door_move_right.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_header_door(td, door)

def test_draw_header_door_init():
    with pytest.raises(ValueError):
        HeaderDoor(90, 2170, 2630)