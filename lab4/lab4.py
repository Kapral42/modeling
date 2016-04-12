#!/usr/bin/python

import sys
import random
import numpy as np

#ATED_NUMBER 10000000
#idefine MAX_MATRIX 10

mat_size = 10
numbers = 10000000
#numbers = 100000

#mat_event = \
#  [
#     [0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2], \
#     [0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \
#     [0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \
#     [0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], \
#     [0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0, 0.0], \
#     [0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0, 0.0], \
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0, 0.0], \
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5, 0.0], \
#     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3, 0.5], \
#     [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.3]  \
#   ]
mat_event = \
    [
        [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \
        [0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \
        [0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], \
        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], \
        [0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], \
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0, 0.0], \
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0, 0.0], \
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5, 0.0], \
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.5], \
        [0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5]  \
    ]

hist_x = [0] * mat_size
hist_event = [0] * mat_size

mat_prob = [0.0] * mat_size
for i in range(mat_size):
    mat_prob[i] = [0.0] * mat_size

array_ksi = [0.0] * 500
random.seed()

for i in range(mat_size):
    mat_prob[i][0] = mat_event[i][0]
    for j in range(mat_size)[1:]:
        mat_prob[i][j] = mat_event[i][j] + mat_prob[i][j - 1]
    # print mat_prob[i]

c_event = 0
for k in range(numbers):
    tmp = random.uniform(0, 1)
    for i in range(mat_size):
        if tmp < mat_prob[c_event][i]:
            c_event = i
            while True:
                ksi = random.uniform(0, 1)
                ksi = -1.0 * np.log(ksi)
                c_x = int(ksi / 0.7)
                if c_x < mat_size:
                    break
            hist_event[c_event] += 1
            hist_x[c_x] += 1
            break
    if k < 500:
        array_ksi[k] = ksi

for i in range(mat_size):
    print i + 1, hist_event[i]
print
for i in range(mat_size):
    print i + 1, hist_x[i]
file = open('ksi.res', 'w')
for i in range(500):
    file.write(str(i + 1) + ' ' + repr(array_ksi[i]) + '\n')
file.close()

