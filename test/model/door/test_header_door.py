from multiprocessing.sharedctypes import Value
from model.door import HeaderDoor, HeaderDoorComponents
from utility.draw.draw_for_test import draw_component
import pytest 


def test_draw_header_door():
    door = HeaderDoor(2630, 930, 2170)
    door.group()
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "header_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_component(td, door)

def test_draw_header_door_move_right():
    door = HeaderDoor(2630, 930, 2170)
    door.group()
    door.move_right(300)
    door.bottom_plate.move_right(300)
    door.top_plate.move_right(300)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "header_door_move_right.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_component(td, door)

def test_draw_header_door_init():
    with pytest.raises(ValueError):
        HeaderDoor(2630, 90, 2170)