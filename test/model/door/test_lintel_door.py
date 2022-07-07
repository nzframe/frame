from model.door import LintelDoor, LintelDoorComponents
from utility.draw.draw_lintel_door import draw_lintel_door

def test_draw_lintel_door():
    door = LintelDoor(1830, 2170, 2630)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "litel_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_lintel_door(td, door)
