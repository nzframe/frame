from model.generic_wall import GenericWall
from dataclasses import dataclass
from typing import List, Callable

from model.timber import Cutted2BY4, CuttedHeader
from model.direction import Orientation
import copy

from utility.draw.draw_header_door import draw_header_door_without
from utility.draw import DrawIT


TRIPPLE_GAP: float = 400

##TODO Fix this hard code
DISTANT_TO_HEADER: float = 170

def move_components():
    pass

def add_header(door_width: float, door_height: float):
    timber = CuttedHeader(door_width + Cutted2BY4.HEIGHT * 2, Orientation.HORIZONTAL)
    timber.move_up(door_height + Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_lintel(door_width: float, door_height:float, distant_to_header: float = DISTANT_TO_HEADER):
    timber = Cutted2BY4(door_width, Orientation.HORIZONTAL)
    timber.move_right(Cutted2BY4.HEIGHT * 2)
    timber.move_up(door_height - distant_to_header)
    return timber

## TODO: need the terms 
def add_top_cripple(door_width: float, door_height: float, distant_to_header: float = DISTANT_TO_HEADER):
    top_cripples = []

    left_timber = Cutted2BY4(distant_to_header, Orientation.VERTICAL)
    left_timber.move_right(Cutted2BY4.HEIGHT * 2)
    left_timber.move_up(door_height - distant_to_header + Cutted2BY4.HEIGHT)
    top_cripples.append(left_timber)

    right_timber = Cutted2BY4(distant_to_header, Orientation.VERTICAL)
    right_timber.move_right(door_width + Cutted2BY4.HEIGHT)
    right_timber.move_up(door_height - distant_to_header + Cutted2BY4.HEIGHT)
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


@dataclass
class HeaderDoorComponents():
    left_trimmer_stud: Cutted2BY4
    right_trimmer_stud: Cutted2BY4

    header: CuttedHeader
    linter: Cutted2BY4
    top_cripples: List[Cutted2BY4] 


HeaderDoorCreateFactory = Callable[[float, float, float], HeaderDoorComponents]

def create_header_door(door_width: float, door_height: float, floor_height: float):
    left_trimmer_stud = add_left_trimmer_stud(door_height)
    right_trimmer_stud = add_right_trimmer_stud(door_height, door_width)

    header = add_header(door_width, door_height)
    lintel = add_lintel(door_width, door_height)

    top_cripples = add_top_cripple(door_width, door_height)

    return HeaderDoorComponents(left_trimmer_stud, right_trimmer_stud, header, lintel, top_cripples)


class HeaderDoor(GenericWall): 
    """
        ___________
        |~~~~~~~~~|
        ||| | | |||
        ||~~~~~~~||
        ||       ||
        ||       ||
        ___________
    """ 

    def __init__(self, door_width: float, door_height: float, floor_height: float):
        self.door_width: float = door_width
        self.door_height: float = door_height
        self.floor_height: float = floor_height
        self.components: HeaderDoorComponents = None
        self.create()
        self.add_top_plate(door_width, floor_height)
        self.add_bottom_plate(door_width)
        self.add_left_king_stud(floor_height)
        self.add_right_king_stud(floor_height, door_width)

    def create(self, door_create_factory: HeaderDoorCreateFactory = create_header_door):
        self.components = door_create_factory(self.door_width, self.door_height, self.floor_height)

    def add_top_plate(self, door_width: float, floor_height: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self, door_width: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*4, Orientation.HORIZONTAL)
        self.bottom_plate = timber

    def add_left_king_stud(self, floor_height: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        self.left_king_stud = timber

    def add_right_king_stud(self, floor_height: float, door_width: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(door_width + Cutted2BY4.HEIGHT * 3)
        self.right_king_stud = timber

    def move_right(self, value: float):
        super().move_right(value)
        door_cpnt = self.components
        door_cpnt.left_trimmer_stud.move_right(value)
        door_cpnt.right_trimmer_stud.move_right(value)
        door_cpnt.header.move_right(value)
        door_cpnt.linter.move_right(value)

        for cripple in door_cpnt.top_cripples:
            cripple.move_right(value)

        return self

    def draw(self, td: DrawIT):
        draw_header_door_without(td, self)