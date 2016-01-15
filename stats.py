# -*- coding: utf-8 -*-

def mean(vals):
    #Calculate the arithmetic mean of a list
    assert type(vals) is list, 'wrong input format'
    vals = [float(x) for x in vals]
    total = sum(vals)
    length = len(vals)
    if length == 0:
        return 0.0
    else:
        return total/length

#print(mean([2,4]))
#print(mean("hello"))
