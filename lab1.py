#!/usr/bin/python

import random

def my_rand():
    """docstring for my_rand"""

    a = 0.63
    up_bound = a
    flg = False
    while not flg:
        x = random.uniform(a, 4*a)
        y = random.uniform(0, up_bound)

        if x <= 2*a:
            if y <= 0.33*x + 0.21:
                flg = True
        else:
            if y <= -0.16*x + 0.83:
                flg = True
    # print x, y
    return x


print my_rand()
