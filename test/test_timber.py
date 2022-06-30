import pytest
from model.timber import CuttedTimber, LeftOuterStud, Orientation, Stud, Plate, TopPlate, LengthLessThanZeroError
from utility.location import XYCoordinate


def test_cutted_timber_default_value():
    cutted_timber = CuttedTimber(2330)
    assert cutted_timber.timber.timber_size.height == 45
    assert cutted_timber.timber.timber_size.width == 90


def test_stud():
    assert Stud(1330).orientation == Orientation.VERTICAL


def test_plate():
    assert Plate(1330).orientation == Orientation.HORIZONTAL


def test_plate_height():
    assert Plate(1380).timber.timber_size.height == 45


def test_timber_purpuse_topplate():
    assert TopPlate(1330).purpose() == "TopPlate"

def test_timber_purpuse_leftstud():
    assert LeftOuterStud(1330).purpose() == "LeftOuterStud"

def test_timber_length_less_than_0():
    with pytest.raises(LengthLessThanZeroError):
        TopPlate(-1)

def test_timber_coordinate():
    cutted_timber = CuttedTimber(2330)
    assert cutted_timber.c_cord == None

def test_plate_coordinate():
    plate = Plate(1380)
    assert plate.c_cord == XYCoordinate(1380, 45)

def test_stud_coordinate():
    stud = Stud(1380)
    assert stud.c_cord == XYCoordinate(45, 1380)