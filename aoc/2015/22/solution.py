from itertools import permutations
from dataclasses import dataclass
from typing import Callable, DefaultDict, List
from colorama import Fore, Style
import random


@dataclass
class Entity:
    hp: int
    mana: int = 0
    attack: int = 0
    armor: int = 0
    spent: int = 0


@dataclass
class Spell:
    cost: int
    timer: int


NEXT_ACTION = {
    'MISSILE':  'DRAIN',
    'DRAIN':    'SHIELD',
    'SHIELD':   'POISON',
    'POISON':   'RECHARGE',
    'RECHARGE': 'MISSILE'
}


def battle(actions, part2=False):
    boss = Entity(71, attack=10)
    # boss = Entity(55, attack=8)
    player = Entity(50, mana=500)

    spells = {
        # name: [cost, ticks_left]
        'MISSILE':  Spell(53, 0),
        'DRAIN':    Spell(73, 0),
        'SHIELD':   Spell(113, 0),
        'POISON':   Spell(173, 0),
        'RECHARGE': Spell(229, 0),
    }

    turn, turn_c = 0, 0
    my_turn = True

    while True:
        if len(actions) - 1 < turn_c:
            return 0

        if spells['POISON'].timer:
            spells['POISON'].timer -= 1
            boss.hp -= 3

        if spells['SHIELD'].timer:
            spells['SHIELD'].timer -= 1
            player.armor = 7
        else:
            player.armor = 0

        if spells['RECHARGE'].timer:
            spells['RECHARGE'].timer -= 1
            player.mana += 101

        if my_turn:

            if part2:
                player.hp -= 1
                if player.hp <= 0:
                    return 0

            # select spell

            spell_name = actions[turn_c]
            spell = spells[spell_name]
            player.mana -= spell.cost
            player.spent += spell.cost

            # execute spell

            if spell_name == 'MISSILE':
                boss.hp -= 4
            elif spell_name == 'DRAIN':
                boss.hp -= 2
                player.hp += 2
            elif spell_name == 'SHIELD':
                if spell.timer:
                    return 0  # cannot use active effect
                spell.timer = 6
            elif spell_name == 'POISON':
                if spell.timer:
                    return 0  # cannot use active effect
                spell.timer = 6
            elif spell_name == 'RECHARGE':
                if spell.timer:
                    return 0  # cannot use active effect
                spell.timer = 5

            if player.mana < 0:
                return 0

        if boss.hp <= 0:
            return player.spent

        if not my_turn:
            player.hp -= max(boss.attack - player.armor, 1)
            if player.hp <= 0:
                return 0

        if my_turn:
            turn_c += 1
        my_turn = not my_turn
        turn += 1


def iterate_actions(actions: List[str], pos: int):
    actions[pos] = NEXT_ACTION[actions[pos]]

    if actions[pos] == 'MISSILE':
        if pos+1 <= len(actions):
            iterate_actions(actions, pos + 1)


def part1(puzzle_in: str):

    # return 1824

    min_spent = 1000000
    actions = ['MISSILE'] * 14

    for _ in range(7000000):
        iterate_actions(actions, 0)

    for i in range(1000000):
        result = battle(actions)
        if i % 500000 == 0:
            print(10000000 - i)
        if result and result < min_spent:
            min_spent = result
            print(i, min_spent, actions)
        iterate_actions(actions, 0)
    return min_spent


def part2(puzzle_in: str):  # this potentially solves it
    min_spent = 1000000
    actions = ['MISSILE'] * 50

    for _ in range(30000000):
        iterate_actions(actions, 0)

    for i in range(15000000):
        result = battle(actions, part2=True)
        if i % 500000 == 0:
            print(15000000 - i)
        if result and result < min_spent:
            min_spent = result
            print(min_spent)
        iterate_actions(actions, 0)
    return min_spent


def faster_part1(puzzle_in: str):
    raise Exception('not implemented yet')


def faster_part2(puzzle_in: str):
    raise Exception('not implemented yet')


# p1 1824
# p2 1937
