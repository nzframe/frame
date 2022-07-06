from dataclasses import dataclass
from model.timber import CuttedTimber, Cutted2BY4, CuttedLintel
from typing import List, Callable
from model.component import Component
from model.timber import Orientation
import copy


TRIPPLE_GAP: float = 400

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
    jack_studs.append(left_timber)

    right_timber = Cutted2BY4(still_height, Orientation.VERTICAL)
    right_timber.move_up(Cutted2BY4.HEIGHT)
    right_timber.move_right(window_width + Cutted2BY4.HEIGHT)
    jack_studs.append(right_timber)
    
    middle_timber = copy.copy(left_timber)
    while True:
        middle_timber.move_right(TRIPPLE_GAP)

        if middle_timber.a_cord < right_timber.a_cord:
            jack_studs.append(middle_timber)
        else:
            break

        jack_studs.append(middle_timber)
        middle_timber = copy.copy(middle_timber)
    
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
    
    middle_timber = copy.copy(left_timber)
    while True:
        middle_timber.move_right(TRIPPLE_GAP)

        if middle_timber.a_cord < right_timber.a_cord:
            top_cripples.append(middle_timber)
        else:
            break

        top_cripples.append(middle_timber)
        middle_timber = copy.copy(middle_timber)
    
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

def add_top_plate(window_width: float, floor_height: float) -> CuttedTimber:
    """_summary_

    Args:
        window_width (float): the width of the door
        floor_height (float): the height of the floor 
    """    """ """
    timber = Cutted2BY4(window_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
    timber.move_up(floor_height + Cutted2BY4.HEIGHT)
    return timber
    

def add_bottom_plate(window_width: float) -> CuttedTimber:
    """_summary_

    Args:
        window_width (float): the width of the door
    """    """ """
    timber = Cutted2BY4(window_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
    return timber

def add_left_kind_stud(floor_height: float):
    """_summary_

    Args:
        door_width (float): the width of the door
        floor_height (float): the height of the floor 
    """    """ """
    timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    return timber

def add_right_kind_stud(floor_height: float, window_width: float):
    """_summary_

    Args:
        door_width (float): the width of the door
        floor_height (float): the height of the floor 
    """    """ """
    timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(window_width + Cutted2BY4.HEIGHT * 3)
    return timber


@dataclass
class WindowComponents():
    top_plate: CuttedTimber
    bottom_plate: CuttedTimber

    left_king_stud: CuttedTimber
    right_king_stud: CuttedTimber

    left_trimmer_stud: CuttedTimber
    right_trimmer_stud: CuttedTimber

    lintel: CuttedTimber
    top_cripples: List[CuttedTimber] 

    still: CuttedTimber

    bottom_jack_studs: List[CuttedTimber] = None
    

WindowCreateFactory = Callable[[float, float, float], WindowComponents]

def create_window(lintel_height: float, still_height: float, window_width: float, floor_height:float):
    top_plate = add_top_plate(window_width, floor_height)
    bottom_plate = add_bottom_plate(window_width)

    left_king_stud = add_left_kind_stud(floor_height)
    right_king_stud = add_right_kind_stud(floor_height, window_width)

    left_trimmer_stud = add_left_trimmer_stud(lintel_height)
    right_trimmer_stud = add_right_trimmer_stud(lintel_height, window_width)

    lintel = add_lintel(lintel_height, window_width)

    top_cripples = add_top_cripple(window_width, lintel_height, floor_height)

    still = add_still(window_width, still_height)

    bottom_jack_studs = add_bottom_jack_studs(window_width, still_height)

    return WindowComponents(top_plate, bottom_plate, left_king_stud, right_king_stud, left_trimmer_stud, right_trimmer_stud, lintel, top_cripples, still, bottom_jack_studs)


class Window(Component):
    def __init__(self, lintel_height: float, till_height: float, window_width: float, floor_height: float):
        self.lintel_height: float = lintel_height
        self.till_height: float = till_height
        self.window_width: float = window_width
        self.floor_height: float = floor_height
        self.components: WindowComponents = None
        self.create()

    
    def create(self, window_create_factory: WindowCreateFactory = create_window):
        self.components = window_create_factory(self.lintel_height, self.till_height, self.window_width, self.floor_height)

