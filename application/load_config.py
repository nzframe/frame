import yaml


def load_config_from_yaml(file_path: str):
    with open(file_path, "r") as stream:
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
