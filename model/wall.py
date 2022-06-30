from dataclasses import dataclass
from typing import List
from unittest import case
from utility.location import SpaceRectangle, XYCoordinate
from model.timber import BottomPlate, CuttedTimber, LeftOuterStud, RightOuterStud, TopPlate

@dataclass
class WallInfo:
    width: int
    height: int 

class Wall(SpaceRectangle):
    options = {
        "TopPlate": "top_plate",
        "BottomPlate": "bottom_plate",
        "LeftOuterStud": "left_outer_stud",
        "RightOuterStud": "right_outer_stud"
    }
    def __init__(self, wall_info: WallInfo) -> None:
        self.wall_info = wall_info
        self.cutted_timbers: List[CuttedTimber] = []
        self.top_plate = None
        self.bottom_plate = None
        self.left_outer_stud = None
        self.right_outer_stud = None

        self.a_cord = XYCoordinate(0, 0)
        self.b_cord = XYCoordinate(0, self.wall_info.width)
        self.c_cord = XYCoordinate(self.wall_info.width, self.wall_info.height)
        self.d_cord = XYCoordinate(self.wall_info.height, 0)

    def register(self, cutted_timber: CuttedTimber):
        setattr(self, self.options[cutted_timber.__class__.__name__], cutted_timber)
        self.cutted_timbers.append(cutted_timber)        

    def get_total_timbers(self):
        return len(self.cutted_timbers)
    
    def timbers(self):
        return self.cutted_timbers