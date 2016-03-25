#!/usr/bin/python

import sys
import random

a = 0.63
N = 100000

def my_func(x):

    y = 0.0
    if x <= 2*a:
        y = 0.33*x + 0.21
    elif x > 2*a and x <= 4*a:
        y = -0.16*x + 0.83

    return y

def reject():

    left = a
    right = 4*a
    up = a

    while True:
        x1 = random.uniform(0, 4*a)
        x2 = random.uniform(0, 4*a)
        if not (my_func(left + (right - left)*x1) < up*x2):
            break
    x2 *= up
    x1 = left + (right - left)*x1

    return x1, x2

def reject_check():

    hits = [0]*30
    for i in range(N):
        res = reject()
        #print res
        index = int(res[0]/0.1)
        hits[index] += 1

    out = ''
    for i in range(30):
        out += str(hits[i]) + ' '
    print out

def repeat(n_val):
    residue_chance = 1.0
    chance_hit = [0.0]*n_val
    hit = [0]*n_val

    for i in range(n_val - 1):
        chance_hit[i] = random.uniform(0, 1) % residue_chance
        residue_chance -= chance_hit[i]
    chance_hit[-1] = residue_chance

    for i in range(N):
        chance = random.uniform(0, 1)
        sum = 0.0
        for j in range(n_val):
            sum += chance_hit[j]
            if (chance < sum):
                hit[j] += 1
                break

    for i in range(n_val):
        print i, '\t', chance_hit[i] * N, '\t', hit[i]

def no_repeat(n_val):
    k = 3*n_val/4
    hit = [0]*n_val
    part = N/k + 1

    for i in range(part):
        nums = range(n_val)
        if i == part - 1:
            k = N % k
        for j in range(k):
            p = 1.0 / (n_val - j)
            it = int(random.uniform(0, 1)*1.0/p)
            hit[nums[it]] += 1
            nums.pop(it)

    for i in range(n_val):
        print i, '\t', hit[i]

def main(argv=None):
    print "Reject method"
    reject_check()
    print "Repeat distribution"
    repeat(10)
    print "Not repeat distribution"
    no_repeat(10)

if __name__ == "__main__":
    sys.exit(main())
