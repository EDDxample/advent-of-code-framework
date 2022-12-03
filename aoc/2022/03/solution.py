import string

priorities = ' ' + string.ascii_lowercase + string.ascii_uppercase


def part1(s: str, ex: str):
    # s = ex  # example mode
    count = 0
    for line in s.splitlines():
        mid = len(line)//2
        h1 = set(line[:mid])

        for item in line[mid:]:
            if item in h1:
                value = priorities.index(item)
                count += value
                break

    return count


def part2(s: str, ex: str):
    # s = ex  # example mode
    it = iter(s.splitlines())

    count = 0
    while line := next(it, None):
        items = {k: 1 for k in line}
        for _ in range(2):
            for item in set(next(it, [])):
                if item in items:
                    items[item] += 1
                    if items[item] == 3:
                        count += priorities.index(item)
    return count


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
