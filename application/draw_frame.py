from psutil import boot_time
from model.direction import Orientation
from model.timber import Cutted2BY4
from utility.draw import DrawIT
from pathlib import Path
import yaml
import importlib

from model.generic_wall import GenericWall
from utility.space.cord import XYCoordinate
from utility.space.rect import XYRectangle
from model.timber import CuttedTimber
import copy

frame_photo_path = Path(__file__).parent / "frame.png" 
config_path = Path(__file__).parent / "config.yml" 
td = DrawIT(frame_photo_path.as_posix())

config = {
    "LintelDoor": "model.door",
    "HeaderDoor": "model.door",
    "DryDoor": "model.door",
    "CommonWall": "model.common",
    "Junction": "model.junction",
    "Window": "model.window",
    "LoadPoint": "model.load_point"
}

def load_yaml(file_path: str):
    with open(file_path, 'r') as stream:
        rt = yaml.safe_load(stream)
    return rt

def prepare_cutted_timber(ct: CuttedTimber, td: DrawIT):
    td.prepare(ct)

def main():
    rt = load_yaml(config_path.as_posix())
    title = rt["title"]
    floor_height = rt["floor_height"]

    total_right_move = 0

    
    index = 0
    start_point: XYCoordinate = None
    end_point: XYCoordinate = None
    for ele in rt["parts"]:
        class_name = ele.pop("type")
        module_name = config[class_name]

        the_class = getattr(importlib.import_module(module_name), class_name)
        instance: GenericWall = the_class(floor_height = floor_height, **ele)
        try:
            instance.move_right(total_right_move)
        except AttributeError:
            print(f"Ingore {class_name} move right function")

        instance.draw(td)

        rect: XYRectangle = instance.get_area
        print(f"the size of the current object: {total_right_move}")
        total_right_move += (rect.b_cord.x - rect.a_cord.x)

        if index == 0:
            start_point = rect.a_cord.x
            print(f"start point cord: {rect.a_cord}")
        elif index == (len(rt["parts"]) - 1):
            end_point = rect.b_cord.x
            print(f"end point cord: {rect.b_cord}")
            # load_point = LoadPoint(2630, 1)
            # junction = Junction(2630, 3)
            # common_wall = CommonWall(600, 2630)
            # lintel_door = LintelDoor(930, 2170, 2630)
            # common_wall2 = CommonWall(600, 2630)
        index = index + 1

    # build the top plate and bottom plate
    print(f"""
            start_point is: {start_point},
            end_point is: {end_point},
            total length of the wall is {end_point - start_point}
        """)
    plate_size = end_point - start_point
    bottom_plate = Cutted2BY4(plate_size, Orientation.HORIZONTAL)
    prepare_cutted_timber(bottom_plate, td)

    top_plate = copy.copy(bottom_plate)
    top_plate.move_up(Cutted2BY4.HEIGHT + floor_height)
    prepare_cutted_timber(top_plate, td)

    td.draw_it()
    
if __name__ == "__main__":
    main()
