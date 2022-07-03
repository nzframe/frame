from model.wall_part import WallPart
from dataclasses import dataclass
from model.direction import Coordination, Offset, Position
from model.timber import CuttedTimber
from typing import List

@dataclass
class WallInfo:
    wall_width: float
    floor_height: float

@dataclass
class DoorComponents:
    left_trimmer_stud: CuttedTimber
    right_trimmer_stud: CuttedTimber
    left_king_stud: CuttedTimber
    right_king_stud: CuttedTimber
    header: CuttedTimber
    top_plate: CuttedTimber
    bottom_plate: CuttedTimber
    top_cripples: List[CuttedTimber] 

class Door(WallPart):
    def __init__(self, window_info: WallInfo) -> None:
        self.window_info = window_info
    
    def create(self, coordinate: Coordination):
        self.coordinate = coordinate
        return self

    def get_offset(self, wall: WallPart, position: Position):
        pass