from coordinates import spaced_coordinate
from model.direction import Orientation

TMPCoordinate = spaced_coordinate("TMPCoordinate", "xy", ordered=True)

class XYCoordinate(TMPCoordinate):
    def __move__(self, x_delta: float = 0, y_delta: float = 0):
        return XYCoordinate(self.x + x_delta, self.y + y_delta)
    
    def move(self, value: float, orientation: Orientation):
        if orientation == Orientation.VERTICAL:
            return self.__move__(y_delta = value)
        elif orientation == Orientation.HORIZONTAL:
            return self.__move__(x_delta = value)
        return self

    def move_up(self, value: float):
        return self.move(value, Orientation.VERTICAL)

    def move_down(self, value: float):
        return self.move(value * -1, Orientation.VERTICAL)

    def move_right(self, value: float):
        return self.move(value, Orientation.HORIZONTAL)
    
    def move_left(self, value: float):
        return self.move(value * -1, Orientation.HORIZONTAL)

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y