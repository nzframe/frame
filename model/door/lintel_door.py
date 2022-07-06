from model.component import Component
from dataclasses import dataclass
from model.timber import CuttedTimber
from typing import List, Callable

from model.timber import Cutted2BY4, CuttedTimber, CuttedLintel
from model.direction import Orientation
import copy

TRIPPLE_GAP: float = 400

def move_components():
    pass

def add_lintel(door_width: float, door_height: float):
    timber = CuttedLintel(door_width + Cutted2BY4.HEIGHT * 2, Orientation.HORIZONTAL)
    timber.move_up(door_height + Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_still():
    pass

def add_top_cripple(door_width: float, door_height: float, floor_height: float):
    top_cripples = []
    left_timber = Cutted2BY4(floor_height - door_height - CuttedLintel.HEIGHT, Orientation.VERTICAL)
    left_timber.move_up(door_height + Cutted2BY4.HEIGHT + CuttedLintel.HEIGHT)
    left_timber.move_right(Cutted2BY4.HEIGHT)
    top_cripples.append(left_timber)

    right_timber = Cutted2BY4(floor_height - door_height - CuttedLintel.HEIGHT, Orientation.VERTICAL)
    right_timber.move_up(door_height + Cutted2BY4.HEIGHT + CuttedLintel.HEIGHT)
    right_timber.move_right(door_width + Cutted2BY4.HEIGHT * 2)
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

def add_left_trimmer_stud(door_height: float):
    """_summary_

    Args:
        door_height (float): _description_

    Returns:
        _type_: _description_
    """    
    timber = Cutted2BY4(door_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_right_trimmer_stud(door_height: float, door_width: float):
    timber = Cutted2BY4(door_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT * 2 + door_width)
    return timber

def add_top_plate(door_width: float, floor_height: float) -> CuttedTimber:
    """_summary_

    Args:
        door_width (float): the width of the door
        floor_height (float): the height of the floor 
    """    """ """
    timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
    timber.move_up(floor_height + Cutted2BY4.HEIGHT)
    return timber
    

def add_bottom_plate(door_width: float) -> CuttedTimber:
    """_summary_

    Args:
        door_width (float): the width of the door
    """    """ """
    timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
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

def add_right_kind_stud(floor_height: float, door_width: float):
    """_summary_

    Args:
        door_width (float): the width of the door
        floor_height (float): the height of the floor 
    """    """ """
    timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(door_width + Cutted2BY4.HEIGHT * 3)
    return timber

@dataclass
class LintelDoorComponents():
    top_plate: CuttedTimber
    bottom_plate: CuttedTimber

    left_king_stud: CuttedTimber
    right_king_stud: CuttedTimber

    left_trimmer_stud: CuttedTimber
    right_trimmer_stud: CuttedTimber

    lintel: CuttedTimber
    top_cripples: List[CuttedTimber] 


LintelDoorCreateFactory = Callable[[float, float, float], LintelDoorComponents]

def create_lintel_door(door_width: float, door_height: float, floor_height: float):
    top_plate = add_top_plate(door_width, floor_height)
    bottom_plate = add_bottom_plate(door_width)

    left_king_stud = add_left_kind_stud(floor_height)
    right_king_stud = add_right_kind_stud(floor_height, door_width)

    left_trimmer_stud = add_left_trimmer_stud(door_height)
    right_trimmer_stud = add_right_trimmer_stud(door_height, door_width)

    header = add_lintel(door_width, door_height)

    top_cripples = add_top_cripple(door_width, door_height, floor_height)

    return LintelDoorComponents(top_plate, bottom_plate, left_king_stud, right_king_stud, left_trimmer_stud, right_trimmer_stud, header, top_cripples)


class LintelDoor(Component):  
    """
    The door structure
        ___________
        ||  |  | ||
        |||||||||||
        ||       ||
        ||       ||
        ||       ||
        ___________
    """ 
    def __init__(self, door_width: float, door_height: float, floor_height: float):
        self.door_width: float = door_width
        self.door_height: float = door_height
        self.floor_height: float = floor_height
        self.door_components: LintelDoorComponents = None

    def create(self, door_create_factory: LintelDoorCreateFactory = create_lintel_door):
        self.door_components = door_create_factory(self.door_width, self.door_height, self.floor_height)
