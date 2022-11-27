from itertools import combinations
from dataclasses import dataclass
from math import ceil


@dataclass
class Entity:
    hp: int
    at: int
    df: int
    cost: int = 0

    def buy(self, cost, at, df):
        self.cost += cost
        self.at += at
        self.df += df


enemy = Entity(100, 8, 2)

weapons = (
    (8, 4, 0),
    (10, 5, 0),
    (25, 6, 0),
    (40, 7, 0),
    (74, 8, 0),
)

armors = (
    (0, 0, 0),
    (13, 0, 1),
    (31, 0, 2),
    (53, 0, 3),
    (75, 0, 4),
    (102, 0, 5),
)

rings = (
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
)


def win(player: Entity):
    ttk_enemy = ceil(100 / max(1, player.at - enemy.df))
    ttk_player = ceil(100 / max(1, enemy.at - player.df))
    return ttk_enemy <= ttk_player


def part1(puzzle_in: str):
    min_cost = 10000
    for weapon in combinations(weapons, 1):
        weapon = weapon[0]
        for armor in combinations(armors, 1):
            armor = armor[0]
            for ringos in combinations(rings, 2):
                player = Entity(100, 0, 0)

                player.buy(*weapon)
                player.buy(*armor)
                player.buy(*ringos[0])
                player.buy(*ringos[1])

                min_cost = min(min_cost, player.cost) if win(player) else min_cost
    return min_cost


def part2(puzzle_in: str):
    max_cost = 0
    for weapon in combinations(weapons, 1):
        weapon = weapon[0]
        for armor in combinations(armors, 1):
            armor = armor[0]
            for ringos in combinations(rings, 2):
                player = Entity(100, 0, 0)

                player.buy(*weapon)
                player.buy(*armor)
                player.buy(*ringos[0])
                player.buy(*ringos[1])

                max_cost = max(max_cost, player.cost) if not win(player) else max_cost
    return max_cost


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')
