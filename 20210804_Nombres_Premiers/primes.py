#!/usr/bin/env python3

from math import isqrt
from datetime import datetime
from typing import List, NoReturn
from argparse import ArgumentParser
from contextlib import contextmanager


FIRST_PRIME = 2

# First step

def is_dividable(candidate: int, divisor: int) -> bool:
    return (candidate % divisor == 0)

# Second step

def is_prime(candidate: int) -> bool:
    # first divisor is 2
    # (can't divide by 0, 1 universal divisor)
    for divisor in range(2, candidate):
        if is_dividable(candidate, divisor):
            return False
    return True

# Third step

def n_first_primes(limit: int) -> NoReturn:
    print('-'*20 + '\n Basic')
    candidate = FIRST_PRIME+1
    # first prime automatically added
    existing = [FIRST_PRIME]
    while len(existing) < limit:
        if is_prime(candidate):
            existing.append(candidate)
        candidate += 1
    # print(existing)

# Fourth step
## 1 - candidate number

def n_first_primes_but_slightly_better(limit: int) -> NoReturn:
    print('-'*20 + '\n Slightly better')
    candidate = FIRST_PRIME+1
    existing = [FIRST_PRIME]
    while len(existing) < limit:
        if is_prime(candidate):
            existing.append(candidate)

        # incrementing by 2, not 1
        # (testing only odd candidates)
        candidate += 2

    # print(existing)

## 2 - divisor number

def is_prime_but_better(candidate: int) -> bool:
    # only testing divisors <= integer square root of candidate
    for divisor in range(2, isqrt(candidate)):
        if is_dividable(candidate, divisor):
            return False
    return True

def n_first_primes_but_really_better(limit: int) -> NoReturn:
    print('-'*20 + '\n Really better')
    candidate = FIRST_PRIME+1
    existing = [FIRST_PRIME]
    while len(existing) < limit:
        if is_prime_but_better(candidate):
            existing.append(candidate)
        candidate += 2
    # print(existing)

## 3 - divisor number

def is_prime_ultimate(candidate: int, existing: List[int]) -> bool:
    # only testing dividor which are primes themselves
    # (existing is the list of calculated primes)
    for divisor in existing:
        if divisor > isqrt(candidate):
            break
        if is_dividable(candidate, divisor):
            return False
    return True

def n_first_primes_ultimate(limit: int) -> NoReturn:
    print('-'*20 + '\n Ultimate')
    candidate = FIRST_PRIME+1
    existing = [FIRST_PRIME]
    while len(existing) < limit:
        if is_prime_ultimate(candidate, existing):
            existing.append(candidate)
        candidate += 2
    # print(existing)

# helper & main code
@contextmanager
def timer():
    start = datetime.now()
    yield
    print('>> Time spent in previous function: {}'.format(datetime.now() - start))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-l', '--limit', type=int, default=None,
                        help='How many primes must be calculated')
    parser.add_argument('-t', '--test', type=int, default=None,
                        help='Is the integer a prime or not')
    arguments = parser.parse_args()

    if arguments.limit is arguments.test is None:
        parser.error('At least one argument is needed')

    if arguments.limit is not None and arguments.test is not None:
        parser.error('"test" and "limit" are mutually exclusive parameters')

    if arguments.limit is not None:
        with timer():
            n_first_primes(arguments.limit)
        with timer():
            n_first_primes_but_slightly_better(arguments.limit)
        with timer():
            n_first_primes_but_really_better(arguments.limit)
        with timer():
            n_first_primes_ultimate(arguments.limit)

    if arguments.test is not None:
        with timer():
            print('{} is a prime number: {}'.format(arguments.test, is_prime(arguments.test)))
