from model.door import LintelDoor
from utility.draw.draw_lintel_door import draw_lintel_door

def test_draw_lintel_door():
    door = LintelDoor(1830, 2170, 2630)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "lintel_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_lintel_door(td, door)

def test_draw_lintel_door_move():
    door = LintelDoor(1830, 2170, 2630)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "lintel_door_move.png" 
    td = DrawIT(file_path.as_posix())
    door.move_right(300)
    draw_lintel_door(td, door)
