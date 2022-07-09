from multiprocessing.sharedctypes import Value
from model.common import CommonWall
from utility.draw.draw_common_wall import draw_common_wall
from utility.draw import DrawIT
from pathlib import Path
import pytest


def test_common_draw_it():
    common_wall = CommonWall(785, 2310)
    file_path = Path(__file__).parent / "common_wall.png" 
    td = DrawIT(file_path.as_posix())
    draw_common_wall(td, common_wall)

def test_common_wall_move_right():
    common_wall = CommonWall(2330, 2310)
    common_wall.move_right(200)
    file_path = Path(__file__).parent / "common_wall_move_right.png" 
    td = DrawIT(file_path.as_posix())
    draw_common_wall(td, common_wall)

    for nogging in common_wall.noggings:
        td.prepare(nogging)
    td.draw_it()

def test_common_wall_init():
    with pytest.raises(ValueError):
        CommonWall(89, 2310)