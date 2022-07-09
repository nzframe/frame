import pytest
from application import get_class_dict


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

def get_wall_instance(type_name, args):
    class_dict = get_class_dict()
    assert len(class_dict) == 7
    wall = class_dict[type_name](**args)
    
    return wall

def test_get_wall_instance():
    config = {'wall_width': 785, 'floor_height': 200}
    instance = get_wall_instance("CommonWall", config)
    assert instance is not None