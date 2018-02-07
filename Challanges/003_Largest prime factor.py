# https://projecteuler.net/problem=4

import numpy as np
from EulerChallanges.Tools.Maths import *

number = 600851475143
# number = 13195
prime_amount = int(np.sqrt(number)) + 1
largest_factor = 0

primes = generate_primes(prime_amount)

while number != 1:
    for p in primes:
        div_num = number / p
        if div_num.is_integer():
            if p > largest_factor:
                largest_factor = p
            number = div_num
            break

print(largest_factor)








