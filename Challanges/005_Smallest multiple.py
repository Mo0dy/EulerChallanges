# https://projecteuler.net/problem=5
import numpy as np


limit = 1e9
possible_numbers = np.arange(2, limit)

for i in range(2, 21):
    possible_numbers = possible_numbers[np.logical_not(possible_numbers % i)]

print("\a")
print(np.min(possible_numbers))
input()
