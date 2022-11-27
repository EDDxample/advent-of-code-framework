import re
import statistics
import math


def part1(s: str, ex: str):
    # s = ex # example mode
    s = [int(x) for x in s.split(',')]  # type: ignore
    med = statistics.median(s)          # type: ignore

    return int(sum([abs(med - x) for x in s]))


def part2(s: str, ex: str):
    # s = ex # example mode
    s = [int(x) for x in s.split(',')]    # type: ignore
    med = math.floor(statistics.mean(s))  # type: ignore
    def get_cost(x, y): return abs(y - x) * (abs(y - x) + 1) / 2
    return int(sum([get_cost(med, x) for x in s]))


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
