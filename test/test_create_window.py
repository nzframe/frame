import pytest
from action.create_window import create_window
from model.wall_part import WallPart, WallInfo
from model.window import Window, WindowInfo
from model.direction import Coordination, Offset, Position


def test_create_window():
    window = create_window(WallPart(WallInfo(1330, 2800)), Window(WindowInfo(250, 440)), Coordination(210, 330))
    assert window.coordinate.x == 210
    assert window.coordinate.y == 330

###TODO
def test_get_offset():
    wall = WallPart(WallInfo(1330, 2800))
    window = Window(WindowInfo(250, 440))
    window = create_window(wall, window, Coordination(210, 330))
