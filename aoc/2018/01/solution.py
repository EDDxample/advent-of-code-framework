def part1(puzzle_in: str):
    return sum(map(int, puzzle_in.splitlines()))


def part2(puzzle_in: str):
    i = 0
    values = {0: 0}
    while True:
        for n in map(int, puzzle_in.splitlines()):
            i += n
            if i in values:
                return i
            values[i] = 0


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
