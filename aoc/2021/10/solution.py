import re

mapping = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def part1(s: str, ex: str):

    score_of = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    # s = ex # example mode
    score = 0
    for line in s.splitlines():
        stack = []
        for c in line:
            if c in mapping:
                stack.append(c)
            elif c == mapping[stack[-1]]:
                stack.pop()
            else:
                # print(f'Expected {mapping[stack[-1]]} but found {c}')
                score += score_of[c]
                break
    return score


def part2(s: str, ex: str):
    score_of = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    # s = ex # example mode
    scores = []
    for line in s.splitlines():
        stack = []
        flag = False
        for c in line:
            if c in mapping:
                stack.append(c)
            elif c == mapping[stack[-1]]:
                stack.pop()
            else:
                # print(f'Expected {mapping[stack[-1]]} but found {c}')
                flag = True
                break
        if not flag and len(stack) > 0:
            local_score = 0
            for c in reversed(stack):
                local_score *= 5
                local_score += score_of[mapping[c]]
            scores.append(local_score)

    return sorted(scores)[int(len(scores) / 2)]


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')
