import re

def part1(puzzle_in: str):
	pos, dep = 0, 0
	for line in puzzle_in.splitlines():
		cmd, value = re.match(r'^(.+)\s(\d+)$', line).groups()
		match (cmd):
			case 'up':      dep -= int(value)
			case 'down':    dep += int(value)
			case 'forward': pos += int(value)
	return pos * dep

def part2(puzzle_in: str):
	pos, dep, aim = 0, 0, 0
	for line in puzzle_in.splitlines():
		cmd, value = re.match(r'^(.+)\s(\d+)$', line).groups()
		match (cmd):
			case 'up':      aim -= int(value)
			case 'down':    aim += int(value)
			case 'forward':
				pos += int(value)
				dep += aim * int(value)
	return pos * dep

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
