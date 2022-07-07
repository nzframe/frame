from dataclasses import dataclass, field

from numpy import block
from model.timber import Cutted2BY4, Orientation
from model.generic_wall import GenericWall
from typing import List, Callable
import copy


BLOCKER_SIZE = 150
BLOCKER_GAP = 250

@dataclass
class JunctionComponents:
    blockers: List[Cutted2BY4] = field(default_factory=list)

class Junction(GenericWall):
    def __init__(self, floor_height: float, number_of_blocks: int = 2):
        self.floor_height = floor_height
        self.number_of_blocks = number_of_blocks
        self.components: JunctionComponents = None
        self.add_top_plate(floor_height)
        self.add_bottom_plate()
        self.add_left_kind_stud()
        self.add_right_kind_stud(floor_height)
        self.create()

    def create(self):
        self.components = self.__create_junction(self.floor_height, self.number_of_blocks)

    def __create_junction(self, floor_height, number_of_stud):
        timbers = []

        blocker = Cutted2BY4(BLOCKER_SIZE, Orientation.VERTICAL)
        blocker.move_up(Cutted2BY4.HEIGHT)
        blocker.move_up(BLOCKER_GAP)
        timbers.append(blocker)

        middle_blocker = blocker

        while True:
            middle_blocker = copy.copy(middle_blocker)
            middle_blocker.move_up(BLOCKER_GAP)
            
            if self.top_plate.a_cord < middle_blocker.d_cord: 
                break
            
            timbers.append(middle_blocker)
        return timbers

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
