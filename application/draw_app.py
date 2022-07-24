from application.wall import Wall
from utility.draw import DrawIT
from application.load_config import load_config_from_yaml


class DrawAPP(Wall):
    def __init__(self, config_path, png_path) -> None:
        super().__init__(config_path, load_config_from_yaml)
        self.td = DrawIT(png_path)

    def draw(self):
        for timber in self.timbers:
            self.td.prepare(timber)

        self.td.draw_it()

    def execute(self):
        super().execute()
        # move first

        # draw
        self.draw()
