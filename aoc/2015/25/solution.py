
def f(steps):
	n = 20151125
	for i in range(steps):
		n = (n * 252533) % 33554393
	return n

def part1(puzzle_in: str):
	x, y = 2978, 3083
	n = x + y - 1
	corner_n = 1 + n * (n - 1) // 2
	return f(corner_n + y - 2)

def part2(puzzle_in: str):
	return 'not implemented yet'

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
