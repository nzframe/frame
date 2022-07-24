import copy
import pytest
from model.timber import Cutted2BY4, distribute_timbers, mmtoft
from model.direction import Orientation
from utility.space.cord import XYCoordinate
import model.timber


def test_cutted_timber_default_value():
    door_width = 1830
    timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT * 4, Orientation.HORIZONTAL)
    assert timber.a_cord == XYCoordinate(0, 0)
    assert timber.b_cord == XYCoordinate(2010, 0)
    assert timber.c_cord == XYCoordinate(2010, 45)
    assert timber.d_cord == XYCoordinate(0, 45)

    timber.move_up(45)

    assert timber.a_cord == XYCoordinate(0, 45)


def test_cutted_timber_less_compare():
    bottom_blocker = Cutted2BY4(250, Orientation.VERTICAL)
    top_blocker = Cutted2BY4(250, Orientation.VERTICAL)
    top_blocker.move_up(100)

    bottom_blocker.move_up(200)
    assert top_blocker.a_cord < bottom_blocker.a_cord


def test_distrubute_blocker():
    start_timber: Cutted2BY4 = Cutted2BY4(200, Orientation.VERTICAL)

    end_timber: Cutted2BY4 = copy.copy(start_timber)
    end_timber.move_up(800)

    rt = [i for i in distribute_timbers(start_timber, end_timber, 300, True)]
    assert len(rt) == 1


def test_distrubute_noggings():
    start_timber: Cutted2BY4 = Cutted2BY4(787, Orientation.HORIZONTAL)

    end_timber: Cutted2BY4 = copy.copy(start_timber)
    end_timber.move_up(787 - 45)

    assert len([i for i in distribute_timbers(start_timber, end_timber, 355)]) == 1


def test_distrubute_cripples():
    start_timber: Cutted2BY4 = Cutted2BY4(200, Orientation.VERTICAL)

    end_timber: Cutted2BY4 = copy.copy(start_timber)
    end_timber.move_right(800)

    assert len([i for i in distribute_timbers(start_timber, end_timber, 300)]) == 2


def test_timber_output(mocker):
    a = Cutted2BY4(27, Orientation.HORIZONTAL)
    mocker.patch.object(a, "a_cord", XYCoordinate(0, 0))
    mocker.patch.object(a, "b_cord", XYCoordinate(3, 0))
    mocker.patch.object(a, "d_cord", XYCoordinate(0, 4))
    assert a.export_revit() == [(0, 0, 0), (mmtoft(3), 0, 0), 0, mmtoft(4)]
