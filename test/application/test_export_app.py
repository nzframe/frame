from application.export_app import ExportAPP
from application.app import App
import application.export_app


def test_app_init(mocker):
    app: App = ExportAPP("./config.yml", './test/application/data')
    mocker.patch(
        'application.export_app.ExportAPP.get_data', return_value = ["results"]
    )
    app.execute()
    assert open("./test/application/data/E1.txt") is not None
    assert open("./test/application/data/E1.txt").readline() == "results"

