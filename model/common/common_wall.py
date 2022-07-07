from ast import Call
from dataclasses import dataclass, field
from model.generic_wall import GenericWall
from model.timber import Cutted2BY4, Orientation
from typing import List, Callable
import  copy
from utility.strategy import gap_strategy_avg, GAP_STRATEGY
from more_itertools import pairwise


STUD_GAP = 355
NOGGING_GAP = 800

@dataclass
class CommonWallComponents:
    studs: List[Cutted2BY4] = field(default_factory=list)

CommonWallCreateFactory = Callable[[float, float, float], CommonWallComponents]

def add_studs(wall_width: float, floor_height: float, stud_gap: float = STUD_GAP):
    studs = []
    left_timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    left_timber.move_up(Cutted2BY4.HEIGHT)

    # right jack stud needs to be added into list last
    studs.append(left_timber)

    right_timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    right_timber.move_up(Cutted2BY4.HEIGHT)
    right_timber.move_right(wall_width - Cutted2BY4.HEIGHT)
    
    middle_timber = copy.copy(left_timber)
    while True:
        middle_timber.move_right(stud_gap)

        if middle_timber.a_cord < right_timber.a_cord:
            studs.append(middle_timber)
        else:
            break

        middle_timber = copy.copy(middle_timber)
    
    # right jack stud needs to be added into list last
    studs.append(right_timber)

    return studs

def create_common_wall(wall_width: float, floor_height: float, stud_gap: float = STUD_GAP) -> CommonWallComponents:
    studs = add_studs(wall_width, floor_height, stud_gap)
    return CommonWallComponents(studs)

class CommonWall(GenericWall):
    def __init__(self, wall_width: float, floor_height: float, stud_gap: float = STUD_GAP, strategy: GAP_STRATEGY = gap_strategy_avg):
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
        self.__create__()

    def __create__(self, common_wall_factory: CommonWallCreateFactory = create_common_wall):
        self.components = common_wall_factory(self.wall_width, self.floor_height, self.stud_gap)
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
            tmp_noggings.append(tmp_nogging)
            tmp_nogging = copy.copy(tmp_nogging)   
        return tmp_noggings      
            
    def add_noggings(self, nogging_gap:float = NOGGING_GAP, gap_strategy: GAP_STRATEGY = gap_strategy_avg):
        if len(self.components.studs) >= 2:
            nogging_gap = gap_strategy(nogging_gap, self.components.studs[-1]-self.components.studs[0])
        for left_stud, right_stud in pairwise(self.components.studs):
            self.noggings.extend(self.__add_noggings(left_stud, right_stud, nogging_gap))