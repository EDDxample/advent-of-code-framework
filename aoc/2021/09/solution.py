import re
from itertools import product


def part1(s: str, ex: str):
    # s = ex # example mode
    heightmap = [[int(n) for n in line] for line in s.splitlines()]
    width, height = len(heightmap[0]), len(heightmap)
    count = 0
    for x, y in product(range(width), range(height)):
        is_low = True
        value = heightmap[y][x]
        if x != 0 and heightmap[y][x - 1] <= value:
            is_low = False
        elif x != width - 1 and heightmap[y][x + 1] <= value:
            is_low = False
        elif y != 0 and heightmap[y - 1][x] <= value:
            is_low = False
        elif y != height - 1 and heightmap[y + 1][x] <= value:
            is_low = False

        if is_low:
            count += 1 + value
    return count


def part2(s: str, ex: str):
    # s = ex # example mode
    heightmap = [[int(n) for n in line] for line in s.splitlines()]
    width, height = len(heightmap[0]), len(heightmap)

    basin_centers = []
    basin_sums = []
    count = 0

    def bfs(x, y):
        visited.add((x, y))
        count = 0
        n = heightmap[y][x]
        def is_higher(i, j): return heightmap[j][i] != 9 and (i, j) not in visited and n < heightmap[j][i]

        if x != 0 and is_higher(x - 1, y):
            count += bfs(x - 1, y)
        if x != width - 1 and is_higher(x + 1, y):
            count += bfs(x + 1, y)
        if y != 0 and is_higher(x, y - 1):
            count += bfs(x, y - 1)
        if y != height - 1 and is_higher(x, y + 1):
            count += bfs(x, y + 1)
        return count + 1

    for x, y in product(range(width), range(height)):
        is_low = True
        value = heightmap[y][x]
        if x != 0 and heightmap[y][x - 1] <= value:
            is_low = False
        elif x != width - 1 and heightmap[y][x + 1] <= value:
            is_low = False
        elif y != 0 and heightmap[y - 1][x] <= value:
            is_low = False
        elif y != height - 1 and heightmap[y + 1][x] <= value:
            is_low = False

        if is_low:
            basin_centers.append((x, y))

    for x, y in basin_centers:
        visited = set()
        basin_sums.append(bfs(x, y))

    result = 1
    for n in sorted(basin_sums)[-3:]:
        result *= n

    return result


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
