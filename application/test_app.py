import pytest

def test_func_params():
    def fun(a, b):
        return a < b

    assert fun(b=2, a=1) == True