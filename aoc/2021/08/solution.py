from collections import defaultdict
from typing import List


def part1(s: str, ex: str):
    # s = ex # example mode
    s = [line.split(' | ')[1] for line in s.splitlines()]  # type: ignore

    count = 0
    for group in s:
        count += len(list(filter(lambda x: len(x) in [2, 3, 4, 7], group.split(' '))))
    return count


def part2(s: str, ex: str):
    total = 0

    def get_collision(arr, brr):
        return list(filter(lambda x: x in brr, arr))

    # Ln = number of n segments
    #
    # base: 1 (L2), 4 (L4), 7 (L3), 8 (L7)
    # 6: L6 that lacks part of 1, also define top and low 1 segments
    # 0: L6 that lacks part of 4
    # 9: last L6
    # 5: L5 that lacks 1's top segment
    # 2: L5 that lacks 1's low segment
    # 3: last L5
    for line in s.splitlines():
        line = [''.join(sorted(c)) for c in line.split(' ')]
        sample, target = line[:10], line[11:]

        top1, low1 = None, None
        L = {5: [], 6: []}
        numbers = {}
        for n in sample:
            l = len(n)
            match (l):
                case 2: numbers[1] = n
                case 3: numbers[7] = n
                case 4: numbers[4] = n
                case 7: numbers[8] = n
                case _: L[l].append(n)

        for n in L[6]:
            collision = get_collision(numbers[1], n)
            if len(collision) == 1:
                numbers[6] = n
                L[6].remove(n)
                low1 = collision[0]
                top1 = [x for x in numbers[1] if x != low1][0]
                print(low1, top1)
                break

        for n in L[6]:
            collision = get_collision(numbers[4], n)
            if len(collision) == 3:
                numbers[0] = n
                L[6].remove(n)
                numbers[9] = L[6].pop()

        for n in L[5]:
            if top1 not in n:
                numbers[5] = n
            elif low1 not in n:
                numbers[2] = n
            else:
                numbers[3] = n

        mappings = {v: k for k, v in numbers.items()}
        result = 0
        for n in target:
            result *= 10
            result += mappings[n]
        total += result
    return total


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
