from action.actions import add_bottom_plate, add_top_plate
from model.wall import Wall, WallInfo
from utility.manager.manager import TimberCheck, Manager
import pytest
from model.timber import TopPlate


def test_timber_check():
    tc = TimberCheck(TopPlate(330))
    tc.scan_type()
    assert TopPlate.TimberTag.PLATE in TopPlate.TimberTag


def test_timber_manager():
    wall: Wall = Wall(WallInfo(280, 640))
    add_top_plate(wall)
    add_bottom_plate(wall)
    manager = Manager(wall)
    sorted_list = manager.sort()
    assert sorted_list != manager.timbers