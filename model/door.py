from sympy import Order
from model.component import Component
from dataclasses import dataclass
from model.timber import CuttedTimber
from typing import List, Callable
from action.action import add_right_kind_stud, add_top_plate, add_bottom_plate, add_left_kind_stud, add_header, add_left_trimmer_stud, add_right_trimmer_stud, add_top_cripple


@dataclass
class DoorComponents():
    top_plate: CuttedTimber
    bottom_plate: CuttedTimber

    left_king_stud: CuttedTimber
    right_king_stud: CuttedTimber

    left_trimmer_stud: CuttedTimber
    right_trimmer_stud: CuttedTimber

    header: CuttedTimber
    top_cripples: List[CuttedTimber] 


DoorCreateFactory = Callable[[float, float, float], DoorComponents]

def create_door(door_width: float, door_height: float, floor_height: float):
    top_plate = add_top_plate(door_width, floor_height)
    bottom_plate = add_bottom_plate(door_width)

    left_king_stud = add_left_kind_stud(floor_height)
    right_king_stud = add_right_kind_stud(floor_height, door_width)

    left_trimmer_stud = add_left_trimmer_stud(door_height)
    right_trimmer_stud = add_right_trimmer_stud(door_height, door_width)

    header = add_header(door_width, door_height)

    top_cripples = add_top_cripple(door_width, door_height, floor_height)

    return DoorComponents(top_plate, bottom_plate, left_king_stud, right_king_stud, left_trimmer_stud, right_trimmer_stud, header, top_cripples)


class LintelDoor(Component):  
    def __init__(self, door_width: float, door_height: float, floor_height: float):
        self.door_width: float = door_width
        self.door_height: float = door_height
        self.floor_height: float = floor_height
        self.door_components: DoorComponents = None

    def create(self, door_create_factory: DoorCreateFactory = create_door):
        self.door_components = door_create_factory(self.door_width, self.door_height, self.floor_height)
