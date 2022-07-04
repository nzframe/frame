from action.action import add_top_plate
from model.direction import Orientation
from model.timber import Cutted2BY4


def test_import_add_header():
    timber = add_top_plate(1830 + 180, 2630)
    assert timber is not None

def test_plus_oprand():
    assert 2304 + Cutted2BY4.HEIGHT == 2349