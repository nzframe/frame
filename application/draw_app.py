from application.wall import Wall, WallInfo
from utility.draw import DrawIT


class DrawAPP(Wall):
    def __init__(self, wall_info: WallInfo, detailed_info, png_path) -> None:
        super().__init__(wall_info, detailed_info)
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
