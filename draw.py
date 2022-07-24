from application.draw_app import DrawAPP
from pathlib import Path
from application.load_config import (
    load_config_from_yaml,
    get_wall_global_info,
    get_wall_detailed_info,
)
from model.wall import Wall, WallInfo

frame_photo_path = Path(__file__).parent / "frame.png"
png_path = frame_photo_path.as_posix()

config_path = Path(__file__).parent / "config.yml"

title, floor_height = get_wall_global_info(config_path, load_config_from_yaml)
wall_info = WallInfo(title, floor_height)
detailed_info = get_wall_detailed_info(config_path, load_config_from_yaml)


def main():
    wall = Wall(wall_info, detailed_info)
    app = DrawAPP(png_path)
    app.prepare(wall)
    app.draw()


if __name__ == "__main__":
    main()
