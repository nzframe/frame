from utility.manager.manager import TimberCheck
import pytest
from model.timber import TopPlate


def test_timber_check():
    tc = TimberCheck(TopPlate(330))
    tc.scan_type()
    assert TopPlate.TimberTag.PLATE in TopPlate.TimberTag
    