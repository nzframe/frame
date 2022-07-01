from coordinates import spaced_coordinate
from dataclasses import dataclass

TMPCoordinate = spaced_coordinate("TMPCoordinate", "xy", ordered=True)

class XYCoordinate(TMPCoordinate):
    def move(self, x_delta: int = 0, y_delta: int = 0):
        return XYCoordinate(self.x + x_delta, self.y + y_delta)
