from model.wall_part import WallPart, WallInfo
from model.window import Window, WindowInfo
from model.direction import Coordination

def create_window(wall: WallPart, window: Window, coordination: Coordination):
    return window.create(coordination)
