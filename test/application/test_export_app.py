from application.export_app import ExportAPP
from application.wall import Wall
from application.load_config import WallInfo


def test_app_init(mocker):
    wall_info = WallInfo("E1", 2630)
    detailed_info = [{"type": "CommonWall", "wall_width": 785}]
    wall = Wall(wall_info, detailed_info)
    app = ExportAPP("./test/application/data")
    mocker.patch.object(
        app,
        "rt",
        [[(1, 2, 3), (4, 5, 6), 7, 8], [(1, 2, 3), (4, 5, 6), 7, 8]],
    )

    app.export(wall)
    assert open("./test/application/data/E1.txt") is not None
