import pytest
from utility.strategy import gap_strategy_avg


def test_avg():
    assert gap_strategy_avg(50, 240) == 48
    assert gap_strategy_avg(800, 355) == 800