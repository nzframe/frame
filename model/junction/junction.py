from dataclasses import dataclass, field
from model.timber import Cutted2BY4, Orientation
from model.generic_wall import GenericWall
from typing import List, Callable
import copy


@dataclass
class JunctionComponents:
    blockers: List[Cutted2BY4] = field(default_factory=list)


JunctionCreateFactory = Callable[[float, float], JunctionComponents]

def create_junction(floor_height, number_of_stud):
    timbers = []

    timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)

    for i in range(1, number_of_stud-1):
        next_timber = copy.copy(timber)
        next_timber.move_right(Cutted2BY4.HEIGHT * i)
        timbers.append(next_timber)

    return timbers

class Junction(GenericWall):
    def __init__(self, floor_height: float, number_of_blocks: int = 2):
        self.floor_height = floor_height
        self.number_of_blocks = number_of_blocks
        self.components: JunctionComponents = None
        self.create()
        self.add_top_plate(floor_height)
        self.add_bottom_plate()
        self.add_left_kind_stud()
        self.add_right_kind_stud(floor_height)


    def create(self, junction_factory: JunctionCreateFactory = create_junction):
        self.components = junction_factory(self.floor_height, self.number_of_blocks)

    def add_top_plate(self, floor_height: float) -> Cutted2BY4:
        """_summary_

        Args:
            window_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(Cutted2BY4.HEIGHT*self.number_of_blocks, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self) -> Cutted2BY4:
        """_summary_

        Args:
            window_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(Cutted2BY4.HEIGHT*self.number_of_blocks, Orientation.HORIZONTAL)
        self.bottom_plate = timber

    def add_left_kind_stud(self):
        """ Junction Wall doesn't have left_king_stud
        """        
        self.left_king_stud = None

    def add_right_kind_stud(self, floor_height: float):
        """ Junction Wall doesn't have right_king_stud
        """        
        self.right_king_stud = None
