from collections import defaultdict
from itertools import permutations
import re

pattern = re.compile(r'(.+) would (lose|gain) (\d+) happiness units by sitting next to (.+)\.\n?')


def part1(puzzle_in: str):
    maxh = None
    people = defaultdict(dict)

    for line in re.findall(pattern, puzzle_in):
        A, sign, val, B = line
        val = int(val) if sign == 'gain' else -int(val)

        try:
            people[A][B] += val
        except:
            people[A][B] = val

        try:
            people[B][A] += val
        except:
            people[B][A] = val

    for route in permutations(people):
        happiness = people[route[0]][route[-1]]
        for i in range(len(route) - 1):
            happiness += people[route[i]][route[i+1]]
        maxh = happiness if maxh is None else max(happiness, maxh)

    return maxh


def part2(puzzle_in: str):
    maxh = None
    people = defaultdict(dict)

    for line in re.findall(pattern, puzzle_in):
        A, sign, val, B = line
        val = int(val) if sign == 'gain' else -int(val)

        try:
            people[A][B] += val
        except:
            people[A][B] = val

        try:
            people[B][A] += val
        except:
            people[B][A] = val

        people['Me'][A] = 0
        people[A]['Me'] = 0

    for route in permutations(people):
        happiness = people[route[0]][route[-1]]
        for i in range(len(route) - 1):
            happiness += people[route[i]][route[i+1]]
        maxh = happiness if maxh is None else max(happiness, maxh)

    return maxh


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
