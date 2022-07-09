from dataclasses import dataclass
from model.direction import Orientation
from model.timber import Cutted2BY4
from utility.draw import DrawIT
from pathlib import Path
import yaml
import copy

frame_photo_path = Path(__file__).parent / "frame.png" 
config_path = Path(__file__).parent / "config.yml" 
td = DrawIT(frame_photo_path.as_posix())


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

        self.current_move = 0
        self.instances = []

    def get_start_point(self):
        return self.instances[0].get_area.a_cord.x

    def get_end_point(self):
        return self.instances[-1].get_area.b_cord.x

    def main(self):
        self.init_each_instance()

        # move first
        for instance in self.instances:
            instance.move_right(self.current_move)
            self.current_move = self.current_move + instance.get_area.b_cord.x - instance.get_area.a_cord.x
        
        # after move, then get the location and get the end point
        plate_size = self.get_end_point() - self.get_start_point()
        plates = self.add_plates(plate_size, self.wall_global_info.floor_height)

        #draw
        self.draw(td, plates)


    def draw(self, td: DrawIT, plates):
        for instance in self.instances:
            instance.draw(td)
        # draw plates
        for plate in plates:
            td.prepare(plate)

        td.draw_it()

    def init_each_instance(self):
        for config in self.wall_detailed_info:
            type_name = config.pop("type")
            config["floor_height"] = self.wall_global_info.floor_height
            self.instances.append(self.get_wall_instance(type_name, config))

    def get_wall_instance(self, type_name, args):
        class_dict = get_class_dict()
        assert len(class_dict) == 7
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

    def add_plates(self, plate_size, floor_height):
        bottom_plate = Cutted2BY4(plate_size, Orientation.HORIZONTAL)

        top_plate = copy.copy(bottom_plate)
        top_plate.move_up(Cutted2BY4.HEIGHT + floor_height)
        
        return [top_plate, bottom_plate]

def main():
    app = App(config_path)
    app.main()
    
if __name__ == "__main__":
    main()
