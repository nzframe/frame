from dataclasses import dataclass, field
from model.generic_wall import GenericWall
from model.timber import Cutted2BY4, Orientation, distribute_timbers
from typing import List, Callable
import  copy
from utility.strategy import gap_strategy_avg, GAP_STRATEGY
from more_itertools import pairwise
import logging

from utility.draw import DrawIT

STUD_GAP = 355
NOGGING_GAP = 800

@dataclass
class CommonWallComponents:
    studs: List[Cutted2BY4] = field(default_factory=list)


class CommonWall(GenericWall):
    def __init__(self, wall_width: float, floor_height: float, stud_gap: float = STUD_GAP, strategy: GAP_STRATEGY = gap_strategy_avg):
        if wall_width <= Cutted2BY4.HEIGHT * 2:
            raise ValueError("Common Wall Width must be greater than 90")
        super().__init__()
        self.wall_width = wall_width
        self.components: CommonWallComponents = []
        self.floor_height = floor_height
        self.stud_gap = strategy(stud_gap, self.wall_width)
        self.add_top_plate(self.wall_width, self.floor_height)
        self.add_bottom_plate(self.wall_width)
        self.add_left_king_stud(self.floor_height)
        self.add_right_king_stud(self.floor_height, self.wall_width)
        self.noggings: List[Cutted2BY4] = []
        self.add_studs(self.wall_width, self.floor_height)

    def add_studs(self, wall_width: float, floor_height: float, stud_gap: float = STUD_GAP):
        studs = []
        left_timber = self.left_king_stud
        right_timber = self.right_king_stud
        
        for middle_timber in distribute_timbers(left_timber, right_timber, stud_gap):
            studs.append(middle_timber)
        
        self.components = CommonWallComponents(studs)

        self.add_noggings(NOGGING_GAP)

    def add_top_plate(self, wall_width: float, floor_height: float) -> Cutted2BY4:
        """_summary_

        Args:
            wall_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(wall_width, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self, wall_width: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(wall_width, Orientation.HORIZONTAL)
        self.bottom_plate = timber

    def add_left_king_stud(self, floor_height: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        self.left_king_stud = timber

    def add_right_king_stud(self, floor_height: float, wall_width: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(wall_width - Cutted2BY4.HEIGHT)
        self.right_king_stud = timber

    def __add_noggings(self, left_stud: Cutted2BY4, right_stud: Cutted2BY4, nogging_gap: float = NOGGING_GAP):                
        nogging_size  = right_stud - left_stud
        
        first_nogging = Cutted2BY4(nogging_size - Cutted2BY4.HEIGHT, Orientation.HORIZONTAL)
        
        first_nogging.move_a_to(left_stud.b_cord)

        tmp_nogging: Cutted2BY4 = first_nogging

        tmp_noggings = []
        while True:
            tmp_nogging.move_up(nogging_gap)
            if left_stud.c_cord < tmp_nogging.d_cord:
                break
            logging.debug(f"{tmp_nogging}")
            tmp_noggings.append(tmp_nogging)
            tmp_nogging = copy.copy(tmp_nogging)   
        return tmp_noggings      
            
    def add_noggings(self, nogging_gap:float = NOGGING_GAP, gap_strategy: GAP_STRATEGY = gap_strategy_avg):
        studs = []
        studs.append(self.left_king_stud)
        studs.extend(self.components.studs)
        studs.append(self.right_king_stud)

        if len(studs) >= 2:
            nogging_gap = gap_strategy(nogging_gap, studs[-1]- studs[0])
        logging.debug(f"{nogging_gap} {studs[-1] - studs[0]}")
        for left_stud, right_stud in pairwise(studs):
            self.noggings.extend(self.__add_noggings(left_stud, right_stud, nogging_gap))

    def move_right(self, value: float):
        super().move_right(value)
        for stud in self.components.studs:
            stud.move_right(value)

        for nogging in self.noggings:
            nogging.move_right(value)

        return self

    def draw(self, td: DrawIT):    
        common_wall_cpnt: CommonWallComponents = self.components
        td.prepare(self.left_king_stud)
        td.prepare(self.right_king_stud)

        for stud in common_wall_cpnt.studs:
            td.prepare(stud)

        for nogging in self.noggings:
            td.prepare(nogging)
