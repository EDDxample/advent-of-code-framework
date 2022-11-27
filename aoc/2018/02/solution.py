from collections import Counter
from difflib import SequenceMatcher


def part1(puzzle_in: str):
    double = 0
    triple = 0
    for id in puzzle_in.splitlines():
        count = Counter(id)
        f2 = f3 = False
        for v in count.values():
            if v == 2 and not f2:
                double += 1
                f2 = True
            if v == 3 and not f3:
                triple += 1
                f3 = True

    return double * triple


def part2(puzzle_in: str):
    id_len = len(puzzle_in.splitlines()[0])

    for i, id in enumerate(puzzle_in.splitlines()):
        sm = SequenceMatcher(a=id)

        for id1 in puzzle_in.splitlines()[i+1:]:
            sm.set_seq2(id1)
            if int(sm.ratio() * id_len) == (id_len - 1):
                s = []
                for a, b in zip(id, id1):
                    if a == b:
                        s.append(a)
                return ''.join(s)


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
