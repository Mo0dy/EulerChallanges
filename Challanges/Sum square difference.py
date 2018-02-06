# https://projecteuler.net/problem=6

import numpy as np


limit = 100

natural_numbers = np.arange(1, limit + 1)

a = np.sum(natural_numbers ** 2)

b = np.sum(natural_numbers) ** 2

print(b - a)


