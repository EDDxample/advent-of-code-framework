import re


def part1(s: str, ex: str):
    # s = ex  # example mode
    count = 0
    p2o = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }
    POINTS = {
        'X': 1,
        'Y': 2,
        'Z': 3,
        'lost': 0,
        'draw': 3,
        'won': 6,
    }
    for line in s.splitlines():
        if not line:
            continue
        a, b = line.split(' ')
        if a == p2o[b]:
            count += POINTS[b] + POINTS['draw']
        elif (b == 'X' and a == 'C') or ord(p2o[b]) - ord(a) == 1:
            count += POINTS[b] + POINTS['won']
        else:
            count += POINTS[b] + POINTS['lost']

    return count


def part2(s: str, ex: str):
    # s = ex  # example mode
    count = 0
    win = {'ABC'[i]: 'BCA'[i] for i in range(3)}
    lose = {'ABC'[i]: 'CAB'[i] for i in range(3)}
    POINTS = {
        'A': 1,
        'B': 2,
        'C': 3,
        'lost': 0,
        'draw': 3,
        'won': 6,
    }
    for line in s.splitlines():
        if not line:
            continue
        a, b = line.split(' ')

        match b:
            case 'X':
                count += POINTS[lose[a]] + POINTS['lost']
            case 'Y':
                count += POINTS[a] + POINTS['draw']
            case _:
                count += POINTS[win[a]] + POINTS['won']

    return count


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
