
def part1(puzzle_in: str):
    previous = None
    count = 0
    for depth in map(int, puzzle_in.splitlines()):
        if previous and previous < depth:
            count += 1
        previous = depth
    return count


def part2(puzzle_in: str):
    depths = list(map(int, puzzle_in.splitlines()))
    previous = None
    count = 0
    for i, depth in enumerate(depths[:-2]):
        current = depth + depths[i+1] + depths[i+2]
        if previous and previous < current:
            count += 1
        previous = current
    return count


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    depths = list(map(int, puzzle_in.splitlines()))
    d0 = depths[0]
    d1 = depths[1]
    count = 0
    for i in range(3, len(depths)):
        if depths[i - 3] < depths[i]:
            count += 1
    return count
