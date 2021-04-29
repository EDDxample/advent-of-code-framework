from hashlib import md5

def part1(puzzle_in: str):
	base = puzzle_in
	for i in range(5000000):
		out = md5((base+str(i)).encode('utf8')).hexdigest()
		if out.startswith('00000'):
			return i
	return 'Not found :('

def part2(puzzle_in: str):
	base = puzzle_in
	for i in range(5000000):
		out = md5((base+str(i)).encode('utf8')).hexdigest()
		if out.startswith('000000'):
			return i
	return 'Not found :('
