from model.door import HeaderDoor, HeaderDoorComponents
from utility.draw.draw_header_door import draw_header_door


def test_draw_header_door():
    door = HeaderDoor(800, 2220, 2310)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "header_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_header_door(td, door)
