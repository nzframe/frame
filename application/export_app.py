from pathlib import Path
from application.wall import load_config_from_yaml, WallInfo


class ExportAPP:
    def __init__(self, data_folder) -> None:
        self.data_folder = data_folder
        self.rt = []

    def export(self, wall):
        file_name = (
            Path(self.data_folder).absolute() / f"{wall.wall_global_info.title}.txt"
        )
        with open(file_name, "w") as file_handler:
            for e in self.rt:
                rt = []
                x, y, z = e[0]
                rt.append(x)
                rt.append(y)
                rt.append(z)
                file_handler.write(f"{x},{y},{z}|")
                x, y, z = e[1]
                file_handler.write(f"{x},{y},{z}|")
                rt.append(x)
                rt.append(y)
                rt.append(z)

                file_handler.write(f"{e[2]}|")
                file_handler.write(f"{e[3]}")
                rt.append(e[2])
                rt.append(e[3])
                print(
                    f"create_wall({rt[0]}, {rt[1]}, {rt[2]}, {rt[3]}, {rt[4]}, {rt[5]}, {rt[6]}, {rt[7]})"
                )
                print(
                    f"create_wall({float(rt[0])*304.8}, {rt[1]}, {rt[2]}, {float(rt[3])*304.8}, {rt[4]}, {rt[5]}, {float(rt[6])*304.8}, {float(rt[7])*304.8})"
                )

                file_handler.write("\n")

    def prepare(self, wall):
        for timber in wall.timbers:
            self.rt.append(timber.export())
