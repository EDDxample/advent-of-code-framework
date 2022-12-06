import re


def part1(s: str, ex: str):
    # s = ex  # example mode
    line = s.strip()
    n = 4
    for i in range(len(line) - n):
        temp = set(line[i:i+n])
        if len(temp) == n:
            print(line[i:i+n])
            return i + n


def part2(s: str, ex: str):
    # s = ex  # example mode
    line = s.strip()
    n = 14
    for i in range(len(line) - n):
        temp = set(line[i:i+n])
        if len(temp) == n:
            print(line[i:i+n])
            return i + n


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
