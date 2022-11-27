import numpy as np


def part1(puzzle_in: str):
    target = 34_000_000
    max_houses = 1_000_000

    houses = np.zeros(max_houses)

    for i in range(1, max_houses):
        houses[i::i] += i * 10
    return np.nonzero(houses >= target)[0][0]


def part2(puzzle_in: str):
    target = 34_000_000
    max_houses = 1_000_000

    houses = np.zeros(max_houses)

    for i in range(1, max_houses):
        houses[i:(i+1)*50:i] += i * 11
    return np.nonzero(houses >= target)[0][0]


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
