from dataclasses import dataclass
from model.timber import CuttedTimber, Cutted2BY4, CuttedLintel, distribute_timbers
from typing import List, Callable
from model.generic_wall import GenericWall
from model.timber import Orientation
import copy
from more_itertools import pairwise

from utility.strategy import GAP_STRATEGY, gap_strategy_avg

from utility.draw import DrawIT

CRIPPLE_GAP: float = 200
NOGGING_GAP: float = 250

def add_lintel(lintel_height: float, window_width: float):
    timber = CuttedLintel(window_width + Cutted2BY4.HEIGHT * 2, Orientation.HORIZONTAL)
    timber.move_up(lintel_height + Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_still(window_width: float, till_height:float):
    timber = Cutted2BY4(window_width, Orientation.HORIZONTAL)
    timber.move_up(till_height + Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT * 2)
    return timber

def add_bottom_jack_studs(window_width: float, still_height: float):
    jack_studs = []
    left_timber = Cutted2BY4(still_height, Orientation.VERTICAL)
    left_timber.move_up(Cutted2BY4.HEIGHT)
    left_timber.move_right(Cutted2BY4.HEIGHT * 2)

    # left jack stud needs to be added into list first
    jack_studs.append(left_timber)

    right_timber = Cutted2BY4(still_height, Orientation.VERTICAL)
    right_timber.move_up(Cutted2BY4.HEIGHT)
    right_timber.move_right(window_width + Cutted2BY4.HEIGHT)
    
    for middle_timber in distribute_timbers(left_timber, right_timber, CRIPPLE_GAP):
        jack_studs.append(middle_timber)
    
    # right jack stud needs to be added into list last
    jack_studs.append(right_timber)

    return jack_studs

def add_top_cripple(window_width: float, lintel_height: float, floor_height: float):
    top_cripples = []
    left_timber = Cutted2BY4(floor_height - lintel_height - CuttedLintel.HEIGHT, Orientation.VERTICAL)
    left_timber.move_up(lintel_height + Cutted2BY4.HEIGHT + CuttedLintel.HEIGHT)
    left_timber.move_right(Cutted2BY4.HEIGHT)
    top_cripples.append(left_timber)

    right_timber = Cutted2BY4(floor_height - lintel_height - CuttedLintel.HEIGHT, Orientation.VERTICAL)
    right_timber.move_up(lintel_height + Cutted2BY4.HEIGHT + CuttedLintel.HEIGHT)
    right_timber.move_right(window_width + Cutted2BY4.HEIGHT * 2)
    top_cripples.append(right_timber)
    
    for middle_timber in distribute_timbers(left_timber, right_timber, CRIPPLE_GAP):
        top_cripples.append(middle_timber)
    
    return top_cripples

def add_left_trimmer_stud(lintel_height: float):
    """_summary_

    Args:
        header_height (float): _description_

    Returns:
        _type_: _description_
    """    
    timber = Cutted2BY4(lintel_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_right_trimmer_stud(lintel_height: float, window_width: float):
    timber = Cutted2BY4(lintel_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT * 2 + window_width)
    return timber


@dataclass
class WindowComponents():
    left_trimmer_stud: CuttedTimber
    right_trimmer_stud: CuttedTimber

    lintel: CuttedTimber
    top_cripples: List[CuttedTimber] 

    still: CuttedTimber

    bottom_jack_studs: List[CuttedTimber] = None
    

WindowCreateFactory = Callable[[float, float, float], WindowComponents]

def create_window(lintel_height: float, still_height: float, window_width: float, floor_height:float):
    left_trimmer_stud = add_left_trimmer_stud(lintel_height)
    right_trimmer_stud = add_right_trimmer_stud(lintel_height, window_width)

    lintel = add_lintel(lintel_height, window_width)

    top_cripples = add_top_cripple(window_width, lintel_height, floor_height)

    still = add_still(window_width, still_height)

    bottom_jack_studs = add_bottom_jack_studs(window_width, still_height)

    return WindowComponents(left_trimmer_stud, right_trimmer_stud, lintel, top_cripples, still, bottom_jack_studs)


class Window(GenericWall):
    def __init__(self, lintel_height: float, till_height: float, window_width: float, floor_height: float):
        if window_width <= 90:
            raise ValueError("WindowDoor width must be greater than 91")
        self.lintel_height: float = lintel_height
        self.till_height: float = till_height
        self.window_width: float = window_width
        self.floor_height: float = floor_height
        self.components: WindowComponents = None
        self.noggings: List[Cutted2BY4] = []
        self.create()
        self.add_top_plate(self.window_width, self.floor_height)
        self.add_bottom_plate(self.window_width)
        self.add_left_king_stud(self.floor_height)
        self.add_right_king_stud(self.floor_height, self.window_width)
        self.add_noggings()

    
    def create(self, window_create_factory: WindowCreateFactory = create_window):
        self.components = window_create_factory(self.lintel_height, self.till_height, self.window_width, self.floor_height)


    def add_top_plate(self, window_width: float, floor_height: float) -> CuttedTimber:
        """_summary_

        Args:
            window_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(window_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self, window_width: float) -> CuttedTimber:
        """_summary_

        Args:
            window_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(window_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
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

    def add_right_king_stud(self, floor_height: float, window_width: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(window_width + Cutted2BY4.HEIGHT * 3)
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
            
    def add_noggings(self, gap_strategy: GAP_STRATEGY = gap_strategy_avg):
        if len(self.components.bottom_jack_studs) >= 2:
            nogging_gap = gap_strategy(NOGGING_GAP, self.components.bottom_jack_studs[-1]-self.components.bottom_jack_studs[0])
        else:
            nogging_gap = NOGGING_GAP
        for left_stud, right_stud in pairwise(self.components.bottom_jack_studs):
            self.noggings.extend(self.__add_noggings(left_stud, right_stud, nogging_gap))

    def move_right(self, value: float):
        super().move_right(value)
        components = self.components

        components.lintel.move_right(value)
        components.still.move_right(value)
        components.left_trimmer_stud.move_right(value)
        components.right_trimmer_stud.move_right(value)

        for cripple in components.top_cripples:
            cripple.move_right(value)

        for jack_stud in components.bottom_jack_studs:
            jack_stud.move_right(value)

        for nogging in self.noggings:
            nogging.move_right(value)
        return self

    def draw(self, td: DrawIT):    
        componenet: WindowComponents = self.components
        td.prepare(self.left_king_stud)
        td.prepare(self.right_king_stud)
        td.prepare(componenet.lintel)
        td.prepare(componenet.still)
        td.prepare(componenet.left_trimmer_stud)
        td.prepare(componenet.right_trimmer_stud)

        for cripple in componenet.top_cripples:
            td.prepare(cripple)

        for jack_stud in componenet.bottom_jack_studs:
            td.prepare(jack_stud)

        for nogging in self.noggings:
            td.prepare(nogging)

