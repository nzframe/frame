from enum import Enum
from dataclasses import dataclass

class Orientation(Enum):
    VERTICAL = 1
    HORIZONTAL = 2

class Position(Enum):
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4

@dataclass
class Coordination:
    x: int
    y: int

@dataclass
class Offset:
    value: int
    direction: Position 
