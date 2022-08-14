from random import randint


def random_number_generator(n):
    count = 0
    while count < n:
        yield randint(1, 100)
        count += 1