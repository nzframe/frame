from dataclasses import dataclass
from model.timber import CuttedTimber
from typing import List
from model.component import Component


@dataclass
class WindowComponents():
    bottom_cripples: List[CuttedTimber]
    still: CuttedTimber

class Window(Component):
    def __init__(self, header_height: float, till_height: float, window_width: float, floor_height: float):
        pass
    
    def create(self):
        pass
