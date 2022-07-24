from dataclasses import dataclass
from model.direction import Orientation
from model.timber import Cutted2BY4
import copy
from typing import Callable
from application.load_config import wall_part_factory

CONFIG_LOADING_FUNC = Callable[[str], str]


@dataclass
class WallInfo:
    title: str
    floor_height: float


class Wall:
    def __init__(self, file_path: str, load_config: CONFIG_LOADING_FUNC) -> None:
        self.set_load_config(load_config)
        self.wall_global_info = self.__get_wall_global_info(file_path)
        self.wall_detailed_info = self.__get_wall_detailed_info(file_path)

        self.instances = []
        self.current_move = 0
        self.timbers = []
        self.load_config: CONFIG_LOADING_FUNC = None

    def set_load_config(self, load_config: CONFIG_LOADING_FUNC):
        self.load_config = load_config

    def execute(self):
        self.init_each_instance()
        for instance in self.instances:
            instance.group()
            instance.move_right(self.current_move)
            instance.bottom_plate.move_right(self.current_move)
            instance.top_plate.move_right(self.current_move)
            self.current_move = (
                self.current_move
                + instance.get_area.b_cord.x
                - instance.get_area.a_cord.x
            )

        # after move, then get the location and get the end point
        plate_size = self.get_end_point() - self.get_start_point()
        plates = self.add_plates(plate_size, self.wall_global_info.floor_height)

        for instance in self.instances:
            self.timbers.extend(instance.grouped)

        self.timbers.extend(plates)

    def init_each_instance(self):
        for config in self.wall_detailed_info:
            type_name = config.pop("type")
            config["floor_height"] = self.wall_global_info.floor_height
            self.instances.append(wall_part_factory(type_name, config))

    def __get_wall_global_info(self, file_path: str):
        rt = self.load_config(file_path)
        title = rt["title"]
        floor_height = rt["floor_height"]
        return WallInfo(title, floor_height)

    def __get_wall_detailed_info(self, file_path: str):
        rt = self.load_config(file_path)
        return rt["parts"]

    def get_start_point(self):
        return self.instances[0].get_area.a_cord.x

    def get_end_point(self):
        return self.instances[-1].get_area.b_cord.x

    def add_plates(self, plate_size, floor_height):
        bottom_plate = Cutted2BY4(plate_size, Orientation.HORIZONTAL)

        top_plate = copy.copy(bottom_plate)
        top_plate.move_up(Cutted2BY4.HEIGHT + floor_height)

        return [top_plate, bottom_plate]
