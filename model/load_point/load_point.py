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
    timber.move_up(Cutted2BY4.HEIGHT)

    for i in range(1, number_of_stud-1):
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
        self.add_top_plate(floor_height)
        self.add_bottom_plate()
        self.add_left_kind_stud(floor_height)
        self.add_right_kind_stud(floor_height)


    def create(self, load_point_factory: LoadPointCreateFactory = create_load_point):
        self.components = load_point_factory(self.floor_height, self.number_of_stud)

    def add_top_plate(self, floor_height: float) -> CuttedTimber:
        """_summary_

        Args:
            window_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(Cutted2BY4.HEIGHT*self.number_of_stud, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self) -> CuttedTimber:
        """_summary_

        Args:
            window_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(Cutted2BY4.HEIGHT*self.number_of_stud, Orientation.HORIZONTAL)
        self.bottom_plate = timber

    def add_left_kind_stud(self, floor_height: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        self.left_king_stud = timber

    def add_right_kind_stud(self, floor_height: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(Cutted2BY4.HEIGHT * self.number_of_stud - Cutted2BY4.HEIGHT)
        self.right_king_stud = timber
