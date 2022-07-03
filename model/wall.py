from dataclasses import dataclass
from typing import List
from unittest import case

from utility.space.rect import XYCoordinate, XYRectangle

from model.timber import CuttedTimber

@dataclass
class WallInfo:
    width: float
    height: float 

class Wall(XYRectangle):
    def __init__(self, wall_info: WallInfo) -> None:
        self.wall_info = wall_info
        self.cutted_timbers: List[CuttedTimber] = []

        self.a_cord = XYCoordinate(0, 0)
        self.b_cord = XYCoordinate(self.wall_info.width, 0)
        self.c_cord = XYCoordinate(self.wall_info.width, self.wall_info.height)
        self.d_cord = XYCoordinate(0, self.wall_info.height)

    def register(self, cutted_timber: CuttedTimber):
        if cutted_timber.__class__.__name__ in self.options:
            setattr(self, self.options[cutted_timber.__class__.__name__], cutted_timber)
        self.cutted_timbers.append(cutted_timber)        

    def get_total_timbers(self):
        return len(self.cutted_timbers)
    
    def timbers(self):
        return self.cutted_timbers