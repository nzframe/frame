import pytest
from model.timber.timber import CuttedTimber


def test_cutted_timber_default_value():
    cutted_timber = CuttedTimber(2330)
    assert cutted_timber.timber.timber_size.height == 45
    assert cutted_timber.timber.timber_size.width == 90

