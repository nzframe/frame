from application.app import App
from utility.draw import DrawIT
import yaml


def load_config_from_yaml(file_path: str):
    with open(file_path, "r") as stream:
        rt = yaml.safe_load(stream)
    return rt


class DrawAPP(App):
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
