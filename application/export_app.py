from application.app import App
from utility.draw import DrawIT

class DrawAPP(App):
    def __init__(self, file_path) -> None:
        super().__init__(file_path)

    def draw(self, td: DrawIT):
        for timber in self.timbers:
            td.prepare(timber)

        td.draw_it()

    def execute(self, td):
        super().execute()
        # move first

        #draw
        self.draw(td)
        