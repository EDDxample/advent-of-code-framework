import re


def part1(s: str, ex: str):
    example = False
    crane_section = 8
    crates = [[] for _ in range(9)]
    if example:
        s = ex  # example mode
        crane_section = 3

    for i, line in enumerate(s.splitlines()):
        if i < crane_section:
            x = []
            for j in range(0, len(line), 4):
                if line[j] == '[':
                    crates[j//4].append(line[j+1])
        elif i > crane_section + 1:
            if result := re.match(r'move (\d+) from (\d+) to (\d+)', line):
                to_move, from_id, to_id = list(map(int, result.groups()))
                for _ in range(to_move):
                    crates[to_id-1].insert(0, crates[from_id-1].pop(0))

    return ''.join([x.pop(0) for x in crates if x])


def part2(s: str, ex: str):
    example = False
    crane_section = 8
    crates = [[] for _ in range(9)]
    if example:
        s = ex  # example mode
        crane_section = 3

    for i, line in enumerate(s.splitlines()):
        if i < crane_section:
            x = []
            for j in range(0, len(line), 4):
                if line[j] == '[':
                    crates[j//4].append(line[j+1])
        elif i > crane_section + 1:
            if result := re.match(r'move (\d+) from (\d+) to (\d+)', line):
                to_move, from_id, to_id = list(map(int, result.groups()))
                for j in range(to_move):
                    crates[to_id-1].insert(j, crates[from_id-1].pop(0))

    return ''.join([x.pop(0) for x in crates if x])


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
