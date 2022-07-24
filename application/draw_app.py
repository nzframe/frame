from utility.draw import DrawIT


class DrawAPP:
    def __init__(self, png_path) -> None:
        self.td = DrawIT(png_path)

    def prepare(self, wall):
        for timber in wall.timbers:
            self.td.prepare(timber)

    def draw(self):
        # draw
        self.td.draw_it()
