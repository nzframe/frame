from application.export_app import ExportAPP
from pathlib import Path
from application.wall import (
    load_config_from_yaml,
    get_wall_global_info,
    get_wall_detailed_info,
)
from application.wall import Wall

data_path = Path(__file__).parent / "data"
config_path = Path(__file__).parent / "config.yml"


wall_info = get_wall_global_info(config_path, load_config_from_yaml)
detailed_info = get_wall_detailed_info(config_path, load_config_from_yaml)

app = ExportAPP(data_path)
wall = Wall(wall_info, detailed_info)
app.prepare(wall)
app.export(wall)
