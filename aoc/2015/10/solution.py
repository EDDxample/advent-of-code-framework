import re


def part1(puzzle_in: str):
    for i in range(40):
        new_str = ''
        m = re.findall(r'([0-9])(\1*)', puzzle_in)
        for key, count in m:
            new_str += str(len(count) + 1) + key
        puzzle_in = new_str
    return len(puzzle_in)


def part2(puzzle_in: str):
    for i in range(50):
        new_str = ''
        m = re.findall(r'([0-9])(\1*)', puzzle_in)
        for key, count in m:
            new_str += str(len(count) + 1) + key
        puzzle_in = new_str
    return len(puzzle_in)


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
