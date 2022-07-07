from model.generic_wall import GenericWall
from dataclasses import dataclass
from typing import List, Callable

from model.timber import Cutted2BY4
from model.direction import Orientation
import copy
from utility.draw import DrawIT


##TODO Fix this hard code
TRIPPLE_GAP: float = 400
DISTANT_TO_HEADER: float = 260

def add_lintel(door_width: float, door_height:float, distant_to_header: float = DISTANT_TO_HEADER):
    timber = Cutted2BY4(door_width, Orientation.HORIZONTAL)
    timber.move_right(Cutted2BY4.HEIGHT)
    timber.move_up(door_height - distant_to_header)
    return timber

## TODO: need the terms 
def add_top_cripple(door_width: float, door_height: float, distant_to_header: float = DISTANT_TO_HEADER):
    top_cripples = []

    left_timber = Cutted2BY4(distant_to_header, Orientation.VERTICAL)
    left_timber.move_right(Cutted2BY4.HEIGHT)
    left_timber.move_up(door_height - distant_to_header + Cutted2BY4.HEIGHT)
    top_cripples.append(left_timber)

    right_timber = Cutted2BY4(distant_to_header, Orientation.VERTICAL)
    right_timber.move_right(door_width)
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


@dataclass
class DryDoorComponents():
    linter: Cutted2BY4
    top_cripples: List[Cutted2BY4] 


DryDoorCreateFactory = Callable[[float, float, float], DryDoorComponents]

def create_dry_door(door_width: float, door_height: float, floor_height: float):
    lintel = add_lintel(door_width, door_height)

    top_cripples = add_top_cripple(door_width, door_height)

    return DryDoorComponents(lintel, top_cripples)


class DryDoor(GenericWall): 
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
        self.components: DryDoorComponents = None
        self.create()
        self.add_top_plate(door_width, floor_height)
        self.add_bottom_plate(door_width)
        self.add_left_king_stud(floor_height)
        self.add_right_king_stud(floor_height, door_width)

    def create(self, door_create_factory: DryDoorCreateFactory = create_dry_door):
        self.components = door_create_factory(self.door_width, self.door_height, self.floor_height)

    def add_top_plate(self, door_width: float, floor_height: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*2, Orientation.HORIZONTAL)
        timber.move_up(floor_height + Cutted2BY4.HEIGHT)
        self.top_plate = timber
        

    def add_bottom_plate(self, door_width: float) -> Cutted2BY4:
        """_summary_

        Args:
            door_width (float): the width of the door
        """    """ """
        timber = Cutted2BY4(door_width + Cutted2BY4.HEIGHT*2, Orientation.HORIZONTAL)
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

    def add_right_king_stud(self, floor_height: float, door_width: float):
        """_summary_

        Args:
            door_width (float): the width of the door
            floor_height (float): the height of the floor 
        """    """ """
        timber = Cutted2BY4(floor_height, Orientation.VERTICAL)
        timber.move_up(Cutted2BY4.HEIGHT)
        timber.move_right(door_width + Cutted2BY4.HEIGHT)
        self.right_king_stud = timber

    def move_right(self, value: float):
        super().move_right(value)
        self.components.linter.move_right(value)

        for cripple in self.components.top_cripples:
            cripple.move_right(value)

        return self
    
    def draw(self, td: DrawIT):    
        door_cpnt: DryDoorComponents = self.components
        td.prepare(self.left_king_stud)
        td.prepare(self.right_king_stud)
        td.prepare(door_cpnt.linter)

        for cripple in door_cpnt.top_cripples:
            td.prepare(cripple)

