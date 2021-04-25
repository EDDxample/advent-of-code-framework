import re

pattern = re.compile(r'\\([\\\"]|(x[a-f0-9][a-f0-9]))')

def part1(puzzle_in: str):
	global pattern

	count = 0
	for line in puzzle_in.splitlines():
		pline = line[1:-1]
		pline = re.sub(pattern, '$', pline)

		# print(line, len(line))
		# print(pline, len(pline))

		count += len(line) - len(pline)
	return count

def part2(puzzle_in: str):
	global pattern

	count = 0
	for line in puzzle_in.splitlines():
		pline = repr(line).replace('"', r'\"')

		# print(line, len(line))
		# print(pline, len(pline))

		count += len(pline) - len(line)
	return count

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
