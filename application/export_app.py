from application.app import App
from pathlib import Path

class ExportAPP(App):
    def __init__(self, config_path, data_folder) -> None:
        super().__init__(config_path)
        self.data_folder = data_folder

    def execute(self):
        super().execute()
        self.open_file(self.output_data)
        
    def output_data(self, file_handler):
        for e in self.get_data():
            for ele in e:
                file_handler.write(str(ele))
            file_handler.write("\n")

    def get_data(self):
        for timber in self.timbers:
            yield timber.export()

    def open_file(self, func):
        file = Path(self.data_folder).absolute() / f"{self.wall_global_info.title}.txt" 
        with open(file, "w") as f:
            func(f)