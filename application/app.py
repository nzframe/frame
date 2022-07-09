from dataclasses import dataclass
import yaml

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

@dataclass
class AppInfo:
    title: str
    floor_height: float

class App:
    def __init__(self, file_path) -> None:
        self.wall_global_info = self.__get_wall_global_info(file_path)
        self.wall_detailed_info = self.__get_wall_detailed_info(file_path)

        self.instances = []


    def execute(self):
        self.init_each_instance()


    def init_each_instance(self):
        for config in self.wall_detailed_info:
            type_name = config.pop("type")
            config["floor_height"] = self.wall_global_info.floor_height
            self.instances.append(self.get_wall_instance(type_name, config))

    def get_wall_instance(self, type_name, args):
        class_dict = get_class_dict()
        wall = class_dict[type_name](**args)
        
        return wall

    def __get_wall_global_info(self, file_path):
        rt = load_config(file_path)
        title = rt["title"]
        floor_height = rt["floor_height"]
        return AppInfo(title, floor_height)

    def __get_wall_detailed_info(self, file_path):
        rt = load_config(file_path)
        return rt["parts"]
