# -*- coding: utf-8 -*-

from packaging_tutorial import my_func
import pytest


def test__my_add():
    assert my_func.my_add(1.2, 1.3) == 2.5


def test__my_sub():
    assert my_func.my_sub(1.2, 1.3) == pytest.approx(-0.1)


def test__my_mul():
    assert my_func.my_mul(2.0, 1.3) == 2.6
