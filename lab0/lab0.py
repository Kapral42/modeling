#!/usr/bin/python

import random
import numpy as np

N = 1000000
N_INT = 100
T_SIZE = 4

def x2(set):
    V = 0
    Y = [0 for i in range(N_INT)]
    x = range(N)
    for i in x:
        Y[int(set[i] * N_INT)] += 1

    for y in Y:
        V += y * y / (1.0 / N_INT)

    V = V*1.0/N - N
    return V

def auto_cor(set):
    sumMx = 0.0
    sumDx = 0.0
    for i in set:
        sumMx += i
        sumDx += i * i
    Mx = (sumMx / N)**2
    Dx = sumDx / N - Mx

    cor_set = []
    for i in range(1, T_SIZE):
        cor = 0.0
        for j in range(0, N - i):
            cor += set[j] * set[j + i]
        cor /= N - i
        cor -= Mx
        cor /= Dx - Mx
        cor_set.append(abs(cor))
    return cor_set

# --- Python numeric random
np_array = np.random.uniform(0, 1, N)

# --- Python random
x = range(N)
array = [random.uniform(0,1) for i in x]

print '\nPython numeric random:'
print 'x^2', x2(np_array)
print 'Auto correlation\n', auto_cor(np_array)

print '\nPython random'
print 'x^2', x2(array)
print 'Auto correlation\n', auto_cor(array)

