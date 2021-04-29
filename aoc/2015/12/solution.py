import re, json

num_pattern = re.compile(r'(-?\d+)')

def part1(puzzle_in: str):
	return sum(map(int, re.findall(num_pattern, puzzle_in)))

def part2(puzzle_in: str):
	data: object = json.loads(puzzle_in)
	

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
