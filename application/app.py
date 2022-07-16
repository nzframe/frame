from dataclasses import dataclass
import yaml
from model.direction import Orientation
from model.timber import Cutted2BY4
import copy

def load_config(file_path: str):
    with open(file_path, 'r') as stream:
        rt = yaml.safe_load(stream)
    return rt

def get_class_dict():
    import importlib
    configs = {
        "LintelDoor": "model.door",
        "HeaderDoor": "model.door",
        "DryDoor": "model.door",
        "CommonWall": "model.common",
        "Junction": "model.junction",
        "Window": "model.window",
        "LoadPoint": "model.load_point"
    }
    class_dict = {}
    for class_name, module_name in configs.items():
        class_dict[class_name] = getattr(importlib.import_module(module_name), class_name)
    return class_dict

def get_wall_instance(type_name, args):
    class_dict = get_class_dict()
    wall = class_dict[type_name](**args)
    
    return wall

@dataclass
class AppInfo:
    title: str
    floor_height: float

class App:
    def __init__(self, file_path: str) -> None:
        self.wall_global_info = self.__get_wall_global_info(file_path)
        self.wall_detailed_info = self.__get_wall_detailed_info(file_path)

        self.instances = []
        self.current_move = 0
        self.timbers = []


    def execute(self):
        self.init_each_instance()
        for instance in self.instances:
            instance.group()
            instance.move_right(self.current_move)
            instance.bottom_plate.move_right(self.current_move)
            instance.top_plate.move_right(self.current_move)
            self.current_move = self.current_move + instance.get_area.b_cord.x - instance.get_area.a_cord.x
        
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
            self.instances.append(get_wall_instance(type_name, config))


    def __get_wall_global_info(self, file_path):
        rt = load_config(file_path)
        title = rt["title"]
        floor_height = rt["floor_height"]
        return AppInfo(title, floor_height)

    def __get_wall_detailed_info(self, file_path):
        rt = load_config(file_path)
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