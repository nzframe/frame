from application.export_app import ExportAPP
from pathlib import Path

data_path = Path(__file__).parent / "data" 
config_path = Path(__file__).parent / "config.yml" 


app = ExportAPP(config_path, data_path)
app.execute()