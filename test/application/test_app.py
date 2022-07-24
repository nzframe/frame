from model.wall import wall_part_factory, Wall
from model.wall import get_class_dict
from pathlib import Path
from model.wall import WallInfo


def test_func_params():
    def fun(a, b):
        return a < b

    assert fun(b=2, a=1) == True


def test_get_class_dict():
    assert len(get_class_dict()) == 7


def test_function_pass():
    config = {"wall_width": 785}

    def fun(wall_width):
        return wall_width

    assert fun(**config) == 785


def test_get_wall_instance():
    config = {"wall_width": 785, "floor_height": 200}
    instance = wall_part_factory("CommonWall", config)
    assert instance is not None


def test_app_init():
    wall_info = WallInfo("E1", 2630)
    detailed_info = [{"type": "CommonWall", "wall_width": 785}]

    app = Wall(wall_info, detailed_info)
    assert app.wall_global_info.floor_height == 2630
    assert app.wall_global_info.title == "E1"

    assert isinstance(app.wall_detailed_info, list)

    # assert app.wall_detailed_info[0]["type"] == "CommonWall"
    assert app.wall_detailed_info[0]["wall_width"] == 785


def test_path_lib():
    frame_photo_path = Path(__file__).parent / "frame.png"
    assert isinstance(frame_photo_path, Path)


def test_path_to_str_converstion():
    frame_photo_path = Path(__file__).parent / "frame.png"
    assert str(frame_photo_path) == frame_photo_path.as_posix()
