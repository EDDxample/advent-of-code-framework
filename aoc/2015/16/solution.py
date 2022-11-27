import re
pattern = re.compile(r'(\w+): (\d+),?\s?')

target_aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}


def part1(puzzle_in: str):

    for i, line in enumerate(puzzle_in.splitlines()):
        aunt_id = i + 1
        aunt_data = line.split(': ', 1)[1]

        flags = 0

        for key, val in re.findall(pattern, aunt_data):
            if flags >= 0:
                if target_aunt[key] == int(val):
                    flags += 1
                else:
                    flags = -1

        if flags == 3:
            return aunt_id


def part2(puzzle_in: str):
    for i, line in enumerate(puzzle_in.splitlines()):
        aunt_id = i + 1
        aunt_data = line.split(': ', 1)[1]

        flags = 0

        for key, val in re.findall(pattern, aunt_data):
            if flags >= 0:
                if key in ['cats', 'trees'] and int(val) > target_aunt[key] or \
                        key in ['pomeranians', 'goldfish'] and int(val) < target_aunt[key] or \
                        key not in ['cats', 'trees', 'pomeranians', 'goldfish'] and int(val) == target_aunt[key]:
                    flags += 1
                else:
                    flags = -1

        if flags == 3:
            return aunt_id


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
