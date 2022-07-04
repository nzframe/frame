from dataclasses import dataclass
from model.direction import Coordination, Position
from model.timber import CuttedTimber
from model.door import DoorComponents
from typing import List
from model.wall import WallInfo


@dataclass
class WindowComponents(DoorComponents):
    bottom_cripples: List[CuttedTimber]
    still: CuttedTimber

class Window():
    def __init__(self, header_height: float, till_height: float, window_width: float, floor_height: float):
        pass
    
    def create(self):
        pass
