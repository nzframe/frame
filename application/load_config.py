import yaml
from typing import Callable
from dataclasses import dataclass

CONFIG_LOADING_FUNC = Callable[[str], str]


@dataclass
class WallInfo:
    title: str
    floor_height: float


def load_config_from_yaml(file_path: str):
    with open(file_path, "r") as stream:
        rt = yaml.safe_load(stream)
    return rt


def get_wall_global_info(config_path: str, load_config: CONFIG_LOADING_FUNC):
    rt = load_config(config_path)
    title = rt["title"]
    floor_height = rt["floor_height"]
    return WallInfo(title, floor_height)


def get_wall_detailed_info(config_path: str, load_config: CONFIG_LOADING_FUNC):
    rt = load_config(config_path)
    return rt["parts"]


def get_class_dict():
    import importlib

    configs = {
        "LintelDoor": "model.door",
        "HeaderDoor": "model.door",
        "DryDoor": "model.door",
        "CommonWall": "model.common",
        "Junction": "model.junction",
        "Window": "model.window",
        "LoadPoint": "model.load_point",
    }
    class_dict = {}
    for class_name, module_name in configs.items():
        class_dict[class_name] = getattr(
            importlib.import_module(module_name), class_name
        )
    return class_dict


def wall_part_factory(type_name, args):
    class_dict = get_class_dict()
    wall = class_dict[type_name](**args)

    return wall
