from typing import Callable

import yaml

CONFIG_LOADING_FUNC = Callable[[str], str]


def load_config_from_yaml(file_path: str):
    with open(file_path, "r") as stream:
        rt = yaml.safe_load(stream)
    return rt


def get_wall_global_info(config_path: str, load_config: CONFIG_LOADING_FUNC):
    rt = load_config(config_path)
    title = rt["title"]
    floor_height = rt["floor_height"]
    return title, floor_height


def get_wall_detailed_info(config_path: str, load_config: CONFIG_LOADING_FUNC):
    rt = load_config(config_path)
    return rt["parts"]
