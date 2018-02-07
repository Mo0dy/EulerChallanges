# https://projecteuler.net/problem=10

'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import numpy as np
from EulerChallanges.Tools.Maths import *
import winsound


print(np.sum(prime_list(2e6)))
winsound.Beep(500, 2000)
