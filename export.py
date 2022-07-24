from application.export_revit_app import ExportAPP
from pathlib import Path
from application.load_config import (
    load_config_from_yaml,
    get_wall_global_info,
    get_wall_detailed_info,
)
from model.wall import Wall, WallInfo

data_path = Path(__file__).parent / "data"
config_path = Path(__file__).parent / "config.yml"


title, floor_height = get_wall_global_info(config_path, load_config_from_yaml)
wall_info = WallInfo(title, floor_height)
detailed_info = get_wall_detailed_info(config_path, load_config_from_yaml)

app = ExportAPP(data_path)
wall = Wall(wall_info, detailed_info)
app.prepare(wall)
app.export(wall)
