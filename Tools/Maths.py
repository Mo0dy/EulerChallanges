import numpy as np


# Sieve of Atkin
def prime_list(limit):
    sieve_list = np.arange(2, limit + 1, dtype=np.int64)
    is_prime = np.ones(sieve_list.shape[0], dtype=bool)
    # stores where the currently highest prime is located
    curr_index = 0

    while curr_index < sieve_list.shape[0]:
        p = sieve_list[curr_index]
        index = curr_index + p
        # sieve out all multiple of the prime number
        while index < sieve_list.shape[0]:
            is_prime[index] = False
            index += p

        if curr_index < sieve_list.shape[0] - 1:
            curr_index += 1
        while curr_index < sieve_list.shape[0] and not is_prime[curr_index]:
            curr_index += 1
    return sieve_list[is_prime]


def generate_fibbonaci(limit):
    elements = np.array([0, 1])
    elem = 1
    while elem < limit:
        elem = np.sum(elements)
        elements[0] = elements[1]
        elements[1] = elem
        yield elem


def generate_triangle_numbers(limit):
    curr_index = 2
    number = 1
    while number < limit:
        yield number
        number += curr_index
        curr_index += 1

