from multiprocessing.sharedctypes import Value
from model.common import CommonWall
from utility.draw.draw_for_test import draw_component
from utility.draw import DrawIT
from pathlib import Path
import pytest


def test_common_draw_it():
    common_wall = CommonWall(785, 2310)
    common_wall.group()
    file_path = Path(__file__).parent / "common_wall.png" 
    td = DrawIT(file_path.as_posix())
    draw_component(td, common_wall)

def test_common_wall_move_right():
    common_wall = CommonWall(2330, 2310)
    common_wall.group()
    common_wall.move_right(200)
    common_wall.bottom_plate.move_right(200)
    common_wall.top_plate.move_right(200)

    file_path = Path(__file__).parent / "common_wall_move_right.png" 
    td = DrawIT(file_path.as_posix())
    draw_component(td, common_wall)

    for nogging in common_wall.noggings:
        td.prepare(nogging)
    td.draw_it()

def test_common_wall_init():
    with pytest.raises(ValueError):
        CommonWall(89, 2310)