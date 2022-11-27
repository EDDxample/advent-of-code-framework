from functools import reduce
from itertools import combinations
from operator import mul


packages = [1, 2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]


def part1(puzzle_in: str):
    target = sum(packages) // 3  # 512
    print(target)

    for i in range(len(packages)):
        out = None
        for group in combinations(packages, i):
            if sum(group) == target:
                qe = reduce(mul, group)
                out = qe if not out else min(out, qe)
        if out:
            return out


def part2(puzzle_in: str):
    target = sum(packages) // 4  # 384
    print(target)

    for i in range(len(packages)):
        out = None
        for group in combinations(packages, i):
            if sum(group) == target:
                qe = reduce(mul, group)
                out = qe if not out else min(out, qe)
        if out:
            return out


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
