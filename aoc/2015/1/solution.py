directions = {
	'(': 1,
	')': -1
}

def part1(puzzle_in):
	global directions
	floor = 0

	for char in puzzle_in:
		floor += directions[char]
	return floor

def part2(puzzle_in):
	global directions
	floor = 0

	for i, char in enumerate(puzzle_in):
		floor += directions[char]
		if floor == -1:
			return i + 1
