from application.app import App
from pathlib import Path
from application.load_config import load_config_from_yaml


class ExportAPP(App):
    def __init__(self, config_path, data_folder) -> None:
        super().__init__(config_path, load_config_from_yaml)
        self.data_folder = data_folder

    def execute(self):
        super().execute()
        self.open_file(self.output_data)

    def output_data(self, file_handler):
        for e in self.get_data():
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

    def get_data(self):
        for timber in self.timbers:
            yield timber.export()

    def open_file(self, func):
        file = Path(self.data_folder).absolute() / f"{self.wall_global_info.title}.txt"
        with open(file, "w") as f:
            func(f)
