from model.door import LintelDoor
from utility.draw.draw_for_test import draw_component

def test_draw_lintel_door():
    door = LintelDoor(2630, 1830, 2170)
    door.group()
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "lintel_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_component(td, door)

def test_draw_lintel_door_move():
    door = LintelDoor(2630, 1830, 2170)
    door.group()
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "lintel_door_move.png" 
    td = DrawIT(file_path.as_posix())
    door.move_right(300)
    door.bottom_plate.move_right(300)
    door.top_plate.move_right(300)

    draw_component(td, door)
