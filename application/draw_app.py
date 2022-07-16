from application.app import App
from utility.draw import DrawIT

class DrawAPP(App):
    def __init__(self, config_path, png_path) -> None:
        super().__init__(config_path)
        self.td = DrawIT(png_path)

    def draw(self):
        for timber in self.timbers:
            self.td.prepare(timber)

        self.td.draw_it()

    def execute(self):
        super().execute()
        # move first

        #draw
        self.draw()
        