from model.door import DryDoor, DryDoorComponents
import pytest
from utility.draw.draw_for_test import draw_component


def test_draw_dry_door():
    door = DryDoor(2000, 2170, 2630)
    door.group()
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "dry_door.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_component(td, door)

def test_draw_dry_door_move_right():
    door = DryDoor(800, 2170, 2630)
    door.group()
    door.move_right(400)
    door.bottom_plate.move_right(400)
    door.top_plate.move_right(400)
    from utility.draw import DrawIT
    from pathlib import Path
    file_path = Path(__file__).parent / "dry_door_move_right.png" 
    td = DrawIT(file_path.as_posix())
    
    draw_component(td, door)

def test_draw_dry_door_init():
    with pytest.raises(ValueError):
        door = DryDoor(90, 2170, 2630)
