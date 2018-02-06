import numpy as np


def generate_primes_list(limit):
    primes = [2]
    possible_numbers = np.arange(2, limit)
    while possible_numbers.shape[0] > 0:
        primes.append(possible_numbers[0])
        possible_numbers = possible_numbers[possible_numbers % primes[-1] != 0]
    return primes


# Sieve of Atkin
def fast_prime_list(limit):
    primes = [2, 3, 5]
    sith_list = np.arange(1, limit + 1)
    is_primt = np.zeros(limit)
    for i in range(sith_list.shape[0]):
        r = sith_list[i] % 60
        if r in [1, 13, 17, 29, 37, 41, 53]:
            pass


def generate_fibbonaci(limit):
    elements = np.array([0, 1])
    elem = 1
    while elem < limit:
        elem = np.sum(elements)
        elements[0] = elements[1]
        elements[1] = elem
        yield elem

