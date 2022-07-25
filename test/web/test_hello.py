import pytest
from web.hello import hello_world, app


app.config.update({"TESTING": True})


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def runner():
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/test")
    assert b"Hello World" in response.data


def test_request_json(client):
    response = client.post("/json", json={"a": "b"})
    assert b'{"a":"b"}\n' in response.data


def test_request_wall(client):
    response = client.post("/wall", json='[{"type": "CommonWall", "wall_width": 785}]')
    assert b"CommonWall" in response.data
