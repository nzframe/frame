from application.draw_app import DrawAPP
from pathlib import Path
from application.load_config import (
    load_config_from_yaml,
    get_wall_global_info,
    get_wall_detailed_info,
)


frame_photo_path = Path(__file__).parent / "frame.png"
png_path = frame_photo_path.as_posix()

config_path = Path(__file__).parent / "config.yml"


wall_info = get_wall_global_info(config_path, load_config_from_yaml)
detailed_info = get_wall_detailed_info(config_path, load_config_from_yaml)


def main():
    app = DrawAPP(wall_info, detailed_info, png_path)
    app.execute()


if __name__ == "__main__":
    main()
