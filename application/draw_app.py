from application.app import App
from model.direction import Orientation
from model.timber import Cutted2BY4
from utility.draw import DrawIT
import copy

class DrawAPP(App):
    def __init__(self, file_path) -> None:
        super().__init__(file_path)
        self.current_move = 0

    def draw(self, td: DrawIT, plates):
        for instance in self.instances:
            instance.prepare(td)
        # draw plates
        for plate in plates:
            td.prepare(plate)

        td.draw_it()

    def get_start_point(self):
        return self.instances[0].get_area.a_cord.x

    def get_end_point(self):
        return self.instances[-1].get_area.b_cord.x

    def execute(self, td):
        super().execute()
        # move first
        for instance in self.instances:
            instance.group()
            instance.move_right(self.current_move)
            instance.bottom_plate.move_right(self.current_move)
            instance.top_plate.move_right(self.current_move)
            self.current_move = self.current_move + instance.get_area.b_cord.x - instance.get_area.a_cord.x
        
        # after move, then get the location and get the end point
        plate_size = self.get_end_point() - self.get_start_point()
        plates = self.add_plates(plate_size, self.wall_global_info.floor_height)

        #draw
        self.draw(td, plates)

    def add_plates(self, plate_size, floor_height):
        bottom_plate = Cutted2BY4(plate_size, Orientation.HORIZONTAL)

        top_plate = copy.copy(bottom_plate)
        top_plate.move_up(Cutted2BY4.HEIGHT + floor_height)
        
        return [top_plate, bottom_plate]