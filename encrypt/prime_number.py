import time
import random


def give_me_primes(how_much):
    primes = [2 for x in range(how_much)]
    size = 0
    temp = 2
    while size < how_much:
        if is_prime(temp, primes, size):
            primes[size] = temp
            size += 1
        temp += 1
    return primes


def give_me_primes_faster(how_much):
    primes = [2 for x in range(how_much)]
    size = 0
    temp = 2
    counter = 0
    while size < how_much:
        if counter > how_much * 0.1:
            print("nastepne 10 %")
            counter = 0
        if is_prime_faster(temp, primes, size):
            counter += 1
            primes[size] = temp
            size += 1
        temp += 1
    return primes


def is_prime(number, less_prime, size):
    for x in range(size):
        if number % less_prime[x] == 0:
            return False
    return True


def is_prime_faster(number, less_prime, size):
    max = int(number ** (1 / 2))
    for x in range(size):
        if number % less_prime[x] == 0:
            return False
        if less_prime[x] >= max:
            return True
    return True


def prime_example():
    prime_example_list = [141650939,
                          141650779,
                          141650771,
                          141650753,
                          141650737,
                          99990001,
                          999007,
                          49979687,
                          49979681,
                          49979663,
                          49979653,
                          ]
    return prime_example_list[random.randrange(0, len(prime_example_list))]
