from model.generic_wall import GenericWall
from dataclasses import dataclass
from typing import List, Callable

from model.timber import Cutted2BY4, CuttedHeader, distribute_timbers
from model.direction import Orientation

from utility.draw import DrawIT
from utility.strategy import gap_strategy_avg, GAP_STRATEGY

TRIPPLE_GAP: float = 400

def move_components():
    pass

def add_header(door_width: float, floor_height: float):
    timber = CuttedHeader(door_width + Cutted2BY4.HEIGHT * 2, Orientation.HORIZONTAL)
    timber.move_up(floor_height + Cutted2BY4.HEIGHT - CuttedHeader.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_lintel(door_width: float, door_height:float):
    timber = Cutted2BY4(door_width, Orientation.HORIZONTAL)
    timber.move_right(Cutted2BY4.HEIGHT * 2)
    timber.move_up(door_height + Cutted2BY4.HEIGHT)
    return timber

def add_top_cripple(door_width: float, door_height: float, floor_height: float, gap_strategy: GAP_STRATEGY = gap_strategy_avg):
    top_cripples = []

    left_timber = Cutted2BY4(floor_height - door_height - CuttedHeader.HEIGHT - Cutted2BY4.HEIGHT, Orientation.VERTICAL)
    left_timber.move_right(Cutted2BY4.HEIGHT * 2)
    left_timber.move_up(door_height + 2 * Cutted2BY4.HEIGHT)
    top_cripples.append(left_timber)

    right_timber = Cutted2BY4(floor_height - door_height - CuttedHeader.HEIGHT - Cutted2BY4.HEIGHT, Orientation.VERTICAL)
    right_timber.move_right(door_width + Cutted2BY4.HEIGHT)
    right_timber.move_up(door_height + 2 * Cutted2BY4.HEIGHT)
    top_cripples.append(right_timber)
    
    tripple_gap = gap_strategy(TRIPPLE_GAP, right_timber - left_timber)

    for middle_timber in distribute_timbers(left_timber, right_timber, tripple_gap):
        top_cripples.append(middle_timber)
    
    return top_cripples

def add_left_trimmer_stud(foor_height: float):
    """_summary_

    Args:
        door_height (float): _description_

    Returns:
        _type_: _description_
    """    
    timber = Cutted2BY4(foor_height - CuttedHeader.HEIGHT, Orientation.VERTICAL)
    timber.move_up(Cutted2BY4.HEIGHT)
    timber.move_right(Cutted2BY4.HEIGHT)
    return timber

def add_right_trimmer_stud(floor_height: float, door_width: float):
    timber = Cutted2BY4(floor_height - CuttedHeader.HEIGHT, Orientation.VERTICAL)
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
    left_trimmer_stud = add_left_trimmer_stud(floor_height)
    right_trimmer_stud = add_right_trimmer_stud(floor_height, door_width)

    header = add_header(door_width, floor_height)
    lintel = add_lintel(door_width, door_height)

    top_cripples = add_top_cripple(door_width, door_height, floor_height)

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
        if door_width <= Cutted2BY4.HEIGHT * 2:
            raise ValueError("Header Door Size should be greater than 90")
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
        door_cpnt: HeaderDoorComponents = self.components
        td.prepare(self.left_king_stud)
        td.prepare(self.right_king_stud)
        td.prepare(door_cpnt.left_trimmer_stud)
        td.prepare(door_cpnt.right_trimmer_stud)
        td.prepare(door_cpnt.header)
        td.prepare(door_cpnt.linter)

        for cripple in door_cpnt.top_cripples:
            td.prepare(cripple)

