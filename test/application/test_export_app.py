from application.export_app import ExportAPP
from application.wall import Wall
import application.export_app
from application.load_config import WallInfo


def test_app_init(mocker):
    wall_info = WallInfo("E1", 2630)
    detailed_info = [{"type": "CommonWall", "wall_width": 785}]

    app: Wall = ExportAPP(wall_info, detailed_info, "./test/application/data")
    mocker.patch(
        "application.export_app.ExportAPP.get_data",
        return_value=[[(1, 2, 3), (4, 5, 6), 7, 8], [(1, 2, 3), (4, 5, 6), 7, 8]],
    )
    app.execute()
    assert open("./test/application/data/E1.txt") is not None
