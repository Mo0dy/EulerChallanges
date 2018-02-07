# https://projecteuler.net/problem=9

'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


import numpy as np

goal_num = 1000

possibilites = []

for i in range(334):
    for j in range(i, 500):
        if i + 2 * j > 1000:
            break
        for ii in range(j, 500):
            if i + j + ii == 1000:
                possibilites.append([i, j, ii])
                break

pos = np.array(possibilites)

for p in pos:
    if p[0] ** 2 + p[1] ** 2 == p[2] ** 2:
        print(p[0] * p[1] * p[2])