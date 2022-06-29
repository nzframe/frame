from model.wall import Wall
from dataclasses import dataclass
from model.direction import Coordination, Offset, Position


@dataclass
class WindowInfo:
    width: int
    height: int

class Window:
    def __init__(self, window_info: WindowInfo) -> None:
        self.window_info = window_info
    
    def create(self, coordinate: Coordination):
        self.coordinate = coordinate
        return self

    def get_offset(self, wall: Wall, position: Position):
        pass