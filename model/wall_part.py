from dataclasses import dataclass
from typing import List
from unittest import case

from utility.space.rect import XYCoordinate, XYRectangle

from model.timber import CuttedTimber

class WallPart(XYRectangle):
    """ wall is a combination of WallPart, window and retailing studs and common structure. """
    def __init__(self, timbers: List[CuttedTimber] = []) -> None:
        self.cutted_timbers = timbers

        self.a_cord = XYCoordinate(0, 0)
        self.b_cord = XYCoordinate(0, 0)
        self.c_cord = XYCoordinate(0, 0)
        self.d_cord = XYCoordinate(0, 0)

    def register(self, cutted_timber: CuttedTimber):
        self.cutted_timbers.append(cutted_timber)        

    def get_total_timbers(self):
        return len(self.cutted_timbers)
    
    def timbers(self):
        return self.cutted_timbers