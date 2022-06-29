from dataclasses import dataclass
from typing import List
from unittest import case

from model.timber import BottomPlate, CuttedTimber, LeftOuterStud, RightOuterStud, TopPlate

@dataclass
class WallInfo:
    width: int
    height: int 

class Wall:
    options = {
        "TopPlate": TopPlate,
        "BottomPlate": BottomPlate,
        "LeftOuterStud": LeftOuterStud,
        "RightOuterStud": RightOuterStud
    }

    def __init__(self, wall_info: WallInfo) -> None:
        self.wall_info = wall_info
        self.cutted_timbers: List[CuttedTimber] = []

    def register(self, cutted_timber: CuttedTimber):
        self.cutted_timbers.append(cutted_timber)
        setattr(self, cutted_timber.purpose().lower(), cutted_timber)
        

    def get_total_timbers(self):
        return len(self.cutted_timbers)