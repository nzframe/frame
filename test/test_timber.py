import pytest
from model.timber import CuttedTimber, Orientation, LengthLessThanZeroError
from utility.space.rect import XYCoordinate


def test_cutted_timber_default_value():
    cutted_timber = CuttedTimber(2330)
    assert cutted_timber.timber.timber_size.height == 45
    assert cutted_timber.timber.timber_size.width == 90

