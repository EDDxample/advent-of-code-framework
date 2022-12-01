import re


def part1(s: str, ex: str):
    # s = ex  # example mode
    most = 0
    current = 0
    for line in s.splitlines():
        if not line:
            if most < current:
                most = current
            current = 0
        else:
            current += int(line)

    if most < current:
        most = current
        current = 0
    return most


def part2(s: str, ex: str):
    # s = ex  # example mode
    top1 = 0
    top2 = 0
    top3 = 0
    current = 0
    for line in s.splitlines():
        if not line:
            if top1 < current:
                top1, current = current, top1
            if top2 < current:
                top2, current = current, top2
            if top3 < current:
                top3 = current
            current = 0
        else:

            current += int(line)

    if top1 < current:
        top1, current = current, top1
    if top2 < current:
        top2, current = current, top2
    if top3 < current:
        top3 = current
    out = [top1, top2, top3]
    return out, sum(out)


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
