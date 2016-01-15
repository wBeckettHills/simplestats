# -*- coding: utf-8 -*-

def mean(vals):
    #Calculate the arithmetic mean of a list
    assert type(vals) is list, 'wrong input format'

    total = sum(vals)
    length = len(vals)
    return total/length

def test_mean():
    assert (mean([2,4])) == 3.0
test_mean()

#print(mean([2,4]))
#print(mean("hello"))
