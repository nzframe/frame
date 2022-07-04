from model.component import Component
from dataclasses import dataclass
from model.timber import CuttedTimber
from typing import List


@dataclass
class DoorComponents:
    left_trimmer_stud: CuttedTimber
    right_trimmer_stud: CuttedTimber
    left_king_stud: CuttedTimber
    right_king_stud: CuttedTimber
    header: CuttedTimber
    top_plate: CuttedTimber
    bottom_plate: CuttedTimber
    top_cripples: List[CuttedTimber] 


def door_create_factory():
    pass


class Door(Component):  
    def __init__(self, door_width: float, door_height: float, floor_height: float):
        self.door_width: float = door_width
        self.door_height: float = door_height
        self.floor_height: float = floor_height
        self.door_components: DoorComponents = None

    def create(self, door_create_factory: door_create_factory):
        door_create_factory(self.door_width, self.door_height, self.floor_height)


