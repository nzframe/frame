from application.app import get_class_dict, get_wall_instance, App


def test_func_params():
    def fun(a, b):
        return a < b

    assert fun(b=2, a=1) == True

def test_get_class_dict():
    assert len(get_class_dict()) == 7

def test_function_pass():
    config = {'wall_width': 785}
    def fun(wall_width):
        return wall_width
    assert fun(**config) == 785 

def test_get_wall_instance():
    config = {'wall_width': 785, 'floor_height': 200}
    instance = get_wall_instance("CommonWall", config)
    assert instance is not None

def test_app_init():
    app = App("./config.yml")
    assert app.wall_global_info.floor_height == 2630
    assert app.wall_global_info.title == "E1"

    assert isinstance(app.wall_detailed_info, list)

    assert app.wall_detailed_info[0]["type"] == "CommonWall"
    assert app.wall_detailed_info[0]["wall_width"] == 785

def test_default_app_execute():
    app = App("./config.yml")
    app.execute()
    assert len(app.instances) == 8