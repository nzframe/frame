from pathlib import Path


class ExportDrawingAPP:
    def __init__(self, data_folder) -> None:
        self.data_folder = data_folder
        self.rt = []

    def export(self, wall):
        file_name = (
            Path(self.data_folder).absolute() / f"{wall.wall_global_info.title}.txt"
        )
        with open(file_name, "w") as file_handler:
            rts = []
            for e in self.rt:
                rt = []
                x, y = e[0]
                rt.append(x)
                rt.append(y)
                file_handler.write(f"{x},{y}|")

                file_handler.write(f"{e[1]}|")
                file_handler.write(f"{e[2]}")
                rt.append(e[1])
                rt.append(e[2])
                rts.append(",".join([str(i) for i in rt]))
                file_handler.write("\n")
            print("|".join(rts))

    def prepare(self, wall):
        for timber in wall.timbers:
            self.rt.append(timber.export_drawing())
