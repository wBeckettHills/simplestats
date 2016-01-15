# -*- coding: utf-8 -*-
from stats import mean

def test_mean():
    assert (mean([2,4])) == 3.0
test_mean()

def test_empty_list():
    assert mean([]) == 0.0
test_empty_list()

def test_float_mean():
    assert (mean([5,6])) == 5.5
test_float_mean()