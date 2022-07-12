from dataclasses import dataclass, field

from model.timber import Cutted2BY4, Orientation, distribute_timbers
from model.generic_wall import GenericWall
from typing import List
import copy
from utility.strategy import gap_strategy_default, GAP_STRATEGY

BLOCKER_SIZE = 250
BLOCKER_GAP = 700

@dataclass
class JunctionComponents:
    blockers: List[Cutted2BY4] = field(default_factory=list)

class Junction(GenericWall):
    def __init__(self, floor_height: float, number_of_blocks: int = 2):
        super().__init__()
        self.floor_height = floor_height
        self.number_of_blocks = number_of_blocks
        self.components: JunctionComponents = None
        self.add_top_plate(floor_height)
        self.add_bottom_plate()
        self.add_left_kind_stud()
        self.add_right_kind_stud(floor_height)
        self.create()

    def create(self):
        self.components = self.__create_blockers(self.floor_height, self.number_of_blocks)

    def __create_blockers(self, floor_height, column_of_blockers, gap_stratey: GAP_STRATEGY = gap_strategy_default) -> List[Cutted2BY4]:
        """_summary_

        Args:
            floor_height (_type_): whether using floor_height or top_plate.a.cord as a criteria?
            number_of_stud (_type_): how many columns of blockers to use

        Returns:
            Cutted2BY4: _description_
        """        

        ## TODO: whether using floor_height or top_plate.a.cord as a criteria?
        timbers = []

        bottom_blocker = Cutted2BY4(BLOCKER_SIZE, Orientation.VERTICAL)
        bottom_blocker.move_up(Cutted2BY4.HEIGHT)
        timbers.append(bottom_blocker)

        top_blocker = Cutted2BY4(BLOCKER_SIZE, Orientation.VERTICAL)
        top_blocker.move_up(Cutted2BY4.HEIGHT + floor_height - BLOCKER_SIZE)
        timbers.append(top_blocker)

        block_gap = gap_stratey(BLOCKER_GAP, top_blocker - bottom_blocker)

        for middle_blocker in distribute_timbers(bottom_blocker, top_blocker, block_gap, True):            
            timbers.append(middle_blocker)

        ## add the leftovers

        # replicate a list as the reference
        tmp_timbers = copy.copy(timbers)

        for i in range(1, column_of_blockers):
            for timber in tmp_timbers:
                tmp_timber: Cutted2BY4 = copy.copy(timber)
                tmp_timber.move_right(Cutted2BY4.HEIGHT * i)
                timbers.append(tmp_timber)

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
        timber = Cutted2BY4(self.floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        self.left_king_stud = timber

    def add_right_kind_stud(self, floor_height: float):
        timber = Cutted2BY4(self.floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(self.number_of_blocks*(Cutted2BY4.HEIGHT+1))
        self.right_king_stud = timber

    def group(self):
        components: JunctionComponents = self.components
        for component in components:
            self.grouped.append(component)
 

