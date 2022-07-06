from dataclasses import dataclass, field
from model.timber import Cutted2BY4, CuttedTimber, Orientation
from model.generic_wall import GenericWall
from typing import List, Callable
import copy


@dataclass
class LoadPointComponents:
    pieces: List[CuttedTimber] = field(default_factory=list)


LoadPointCreateFactory = Callable[[float, float], LoadPointComponents]

def create_load_point(floor_height, number_of_stud):
    timbers = []

    timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    timbers.append(timber)
    for i in range(number_of_stud):
        next_timber = copy.copy(timber)
        next_timber.move_right(Cutted2BY4.HEIGHT * i)
        timbers.append(next_timber)

    return timbers

class LoadPoint(GenericWall):
    def __init__(self, floor_height: float, number_of_stud: int = 5):
        self.floor_height = floor_height
        self.number_of_stud = number_of_stud
        self.components: LoadPointComponents = None
        self.create()

    def create(self, load_point_factory: LoadPointCreateFactory = create_load_point):
        self.components = create_load_point(self.floor_height, self.number_of_stud)
