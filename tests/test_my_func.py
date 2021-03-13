# -*- coding: utf-8 -*-

from packaging_tutorial import my_func


def test__my_add():
    assert my_func.my_add(1.2, 1.3) == 2.5


def test__my_sub():
    assert my_func.my_sub(1.2, 1.3) == -0.1
