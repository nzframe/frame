from functools import total_ordering
from utility.space.rect import XYRectangle


@total_ordering
class CuttedTimber(XYRectangle):
    """ cutted timber used to represent the materials used in door, window and retaining studs"""
    def __init__(self, length: float):
        if length < 0:
            raise ValueError("The length of timber can't be negative")
        self.length: float = length


class Cutted2BY4(CuttedTimber):
    NAME: str = "TwoByFour"
    HEIGHT: float = 45
    WIDTH: float = 90
