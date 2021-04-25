from collections import defaultdict
from itertools import permutations


def part1(puzzle_in: str):
	min_cost = -1
	connections = defaultdict(dict)

	for line in puzzle_in.splitlines():
		locs, value = line.split(' = ')
		cityA, cityB = locs.split(' to ')
		connections[cityA][cityB] = int(value)
		connections[cityB][cityA] = int(value)
	
	for route in permutations(connections):
		cost = 0
		for i in range(len(route) - 1):
			cost += connections[route[i]][route[i + 1]]
		
		min_cost = cost if min_cost < 0 else min(min_cost, cost)
	return min_cost

def part2(puzzle_in: str):
	max_cost = 0
	connections = defaultdict(dict)

	for line in puzzle_in.splitlines():
		locs, value = line.split(' = ')
		cityA, cityB = locs.split(' to ')
		connections[cityA][cityB] = int(value)
		connections[cityB][cityA] = int(value)
	
	for route in permutations(connections):
		cost = 0
		for i in range(len(route) - 1):
			cost += connections[route[i]][route[i + 1]]
		
		max_cost = max(max_cost, cost)
	return max_cost

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
