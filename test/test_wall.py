import pytest
from model.wall import WallInfo, Wall

def test_wall_init():
    wall = Wall(WallInfo(width=100, height=100))
    assert wall.wall_info.width == 100
    assert wall.wall_info.height == 100
