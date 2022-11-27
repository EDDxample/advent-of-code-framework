import numpy as np
import re
grid = np.zeros((1000, 1000), dtype=bool)
grid2 = np.zeros((1000, 1000), 'int32')

pattern = re.compile(r'(toggle|turn on|turn off)\s(\d+,\d+) through (\d+,\d+)')


def part1(puzzle_in: str):
    global grid
    for line in puzzle_in.splitlines():
        if m := re.match(pattern, line):
            action = m.group(1)
            x0, y0 = list(map(int, m.group(2).split(',')))
            x1, y1 = list(map(int, m.group(3).split(',')))

            if action == 'turn on':
                grid[x0:x1+1, y0:y1+1] = True
            elif action == 'turn off':
                grid[x0:x1+1, y0:y1+1] = False
            elif action == 'toggle':
                grid[x0:x1+1, y0:y1+1] = ~grid[x0:x1+1, y0:y1+1]
        else:
            raise Exception('wtf')
    return np.count_nonzero(grid)


def part2(puzzle_in: str):
    global grid2

    for line in puzzle_in.splitlines():
        if m := re.match(pattern, line):
            action = m.group(1)
            x0, y0 = list(map(int, m.group(2).split(',')))
            x1, y1 = list(map(int, m.group(3).split(',')))

            if action == 'turn on':
                grid2[x0:x1+1, y0:y1+1] += 1
            elif action == 'turn off':
                grid2[x0:x1+1, y0:y1+1] -= 1
                grid2[grid2 < 0] = 0
            elif action == 'toggle':
                grid2[x0:x1+1, y0:y1+1] += 2
        else:
            raise Exception('wtf')
    return np.sum(grid2)


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
