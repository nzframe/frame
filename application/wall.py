from model.direction import Orientation
from model.timber import Cutted2BY4
import copy
from application.load_config import wall_part_factory, WallInfo


class Wall:
    def __init__(self, wall_info: WallInfo, detailed_info) -> None:
        self.wall_global_info = wall_info
        self.wall_detailed_info = detailed_info

        self.instances = []
        self.current_move = 0
        self.timbers = []
        self.export()

    def export(self):
        self.__init_each_instance()
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
        plate_size = self.__get_end_point() - self.__get_start_point()
        plates = self.__add_plates(plate_size, self.wall_global_info.floor_height)

        for instance in self.instances:
            self.timbers.extend(instance.grouped)

        self.timbers.extend(plates)

    def __init_each_instance(self):
        for config in self.wall_detailed_info:
            type_name = config.pop("type")
            config["floor_height"] = self.wall_global_info.floor_height
            self.instances.append(wall_part_factory(type_name, config))

    def __get_start_point(self):
        return self.instances[0].get_area.a_cord.x

    def __get_end_point(self):
        return self.instances[-1].get_area.b_cord.x

    def __add_plates(self, plate_size, floor_height):
        bottom_plate = Cutted2BY4(plate_size, Orientation.HORIZONTAL)

        top_plate = copy.copy(bottom_plate)
        top_plate.move_up(Cutted2BY4.HEIGHT + floor_height)

        return [top_plate, bottom_plate]
