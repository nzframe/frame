from application.export_app import ExportAPP
from application.wall import Wall
import application.export_app


def test_app_init(mocker):
    app: Wall = ExportAPP("./config.yml", "./test/application/data")
    mocker.patch(
        "application.export_app.ExportAPP.get_data",
        return_value=[[(1, 2, 3), (4, 5, 6), 7, 8], [(1, 2, 3), (4, 5, 6), 7, 8]],
    )
    app.execute()
    assert open("./test/application/data/E1.txt") is not None
