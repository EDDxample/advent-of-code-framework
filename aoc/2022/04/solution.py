import re


def part1(s: str, ex: str):
    # s = ex  # example mode
    count = 0
    for line in s.splitlines():
        if result := re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line):
            s1, e1, s2, e2 = list(map(int, result.groups()))
            if (s1 >= s2 and e1 <= e2) or (s1 <= s2 and e1 >= e2):
                count += 1
    return count


def part2(s: str, ex: str):
    # s = ex  # example mode
    count = 0
    for line in s.splitlines():
        if result := re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line):
            s1, e1, s2, e2 = list(map(int, result.groups()))
            if s1 <= e2 and e1 >= s2:
                count += 1
    return count


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
