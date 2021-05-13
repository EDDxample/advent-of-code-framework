from itertools import combinations
from functools import reduce

def part1(puzzle_in: str):
	arr = list(map(int, puzzle_in.split('\n')))
	target = 150
	if sum(arr) == target: return 1

	count = 0
	for i in range(len(arr) - 1):
		for subarr in combinations(arr, i):
			if sum(subarr) == target:
				count += 1
	return count


def part2(puzzle_in: str):
	arr = list(map(int, puzzle_in.split('\n')))
	target = 150
	if sum(arr) == target: return 1

	count = 0
	for i in range(len(arr) - 1):
		for subarr in combinations(arr, i):
			if sum(subarr) == target:
				count += 1
		if count > 0: return count
	return count

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
