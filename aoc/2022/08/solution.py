DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def part1(s: str, ex: str):
    # s = ex  # example mode

    forest = _parse_input(s)
    count = len(forest) * 2 + (len(forest[0]) - 2) * 2

    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[0]) - 1):

            if _is_visible(forest, i, j):
                count += 1

    return count


def part2(s: str, ex: str):
    # s = ex  # example mode

    forest = _parse_input(s)
    max_score = 0

    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[0]) - 1):

            if _is_visible(forest, i, j):
                max_score = max(max_score, _get_score(forest, i, j))

    return max_score


def faster_part1(s: str, ex: str):
    raise Exception('not implemented yet')


def faster_part2(s: str, ex: str):
    raise Exception('not implemented yet')


def _parse_input(text: str):
    return [list(map(int, line)) for line in text.split("\n") if line]


def _in_bounds(forest: list[list[int]], x: int, y: int) -> bool:
    return 0 <= x < len(forest) and 0 <= y < len(forest[0])


def _is_visible(forest: list[list[int]], i: int, j: int) -> bool:
    visible = [True] * 4
    for index, dir in enumerate(DIRECTIONS):
        dx, dy = dir
        tx, ty = i, j

        while _in_bounds(forest, tx + dx, ty + dy):
            tx += dx
            ty += dy
            if forest[tx][ty] >= forest[i][j]:
                visible[index] = False
                break

    return any(visible)


def _get_score(forest: list[list[int]], i: int, j: int) -> int:
    score = None

    for dx, dy in DIRECTIONS:
        steps = 1

        while flag := _in_bounds(forest, i + dx * steps, j + dy * steps):

            if forest[i + dx * steps][j + dy * steps] >= forest[i][j]:
                break

            steps += 1

        dir_score = steps if flag else steps - 1
        # print(f"dir: {(dx, dy)}, score: {dir_score}")

        if dir_score:
            if score is None:
                score = dir_score
            else:
                score *= dir_score

    return score
