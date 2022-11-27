import re
from itertools import product


def iterXY(x, y): return product(range(x), range(y))


def part1(s: str, ex: str):
    # s = ex # example mode

    s = s.split('\n\n')  # type: ignore
    numbers = [int(x) for x in s[0].split(',')]
    s = s[1:]

    boards = []

    # parse boards
    for i in s:
        i = i.split('\n')
        boards.append([list(map(int, re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*', j[0]).groups())) for j in zip(i, range(5))])  # type: ignore

    # play bingo
    for n in numbers:
        for i in range(len(boards)):
            for x, y in iterXY(5, 5):
                if boards[i][x][y] == n:
                    boards[i][x][y] = -1
            if winning(boards[i], n == 24):
                return unmarked(boards[i]) * n

    return 'not found'


def part2(s: str, ex: str):
    # s = ex # example mode

    s = s.split('\n\n')  # type: ignore
    numbers = [int(x) for x in s[0].split(',')]
    s = s[1:]

    boards = []

    # parse boards
    for i in s:
        i = i.split('\n')
        boards.append([list(map(int, re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*', j[0]).groups())) for j in zip(i, range(5))])  # type: ignore

    winners = []
    last_winner = 0

    # play bingo
    for n in numbers:
        for i in range(len(boards)):
            for x, y in iterXY(5, 5):
                if boards[i][x][y] == n:
                    boards[i][x][y] = -1
            if winning(boards[i], n == 24):
                if i not in winners:
                    winners.append(i)
                    last_winner = unmarked(boards[i]) * n
    return last_winner


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')


def winning(board, log):
    for i in range(5):
        col_won, row_won = True, True
        for j in range(5):
            if board[i][j] != -1:
                row_won = False
            if board[j][i] != -1:
                col_won = False
        if col_won or row_won:
            return True
    return False


def unmarked(board):
    return sum([max(board[x][y], 0) for x, y in iterXY(5, 5)])
