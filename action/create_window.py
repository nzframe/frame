from model.wall import Wall, WallInfo
from model.window import Window, WindowInfo
from model.direction import Coordination

def create_window(wall: Wall, window: Window, coordination: Coordination):
    return window.create(coordination)
