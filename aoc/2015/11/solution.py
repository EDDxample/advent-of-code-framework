import re

pairs_pattern = re.compile(r'.*(\w)\1.*(\w)\2.*')

def increase(password: str):
	out = [ c for c in password ]
	for i in reversed(range(len(password))):
		char = out[i]
		if   char < 'z':
			out[i] = chr(ord(char) + 1)
			return ''.join(out)
		else: out[i] = 'a'

		if i == 0:
			return 'a' + ''.join(out)

def is_valid(password: str):
	a, b = None, None
	triads = False
	for c in password:
		if c in 'iol':
			return False
		if   not a: a = c
		elif not b: b = c
		elif ord(a) == (ord(b) - 1) and ord(a) == (ord(c) - 2):
			triads = True
		else: a, b = b, c

	if not triads:
		return False

	match = re.match(pairs_pattern, password)
	if not match or match[0] == match[1]:
		return False

	return password


def part1(puzzle_in: str):
	return 'hepxxyzz (by hand)'

def part2(puzzle_in: str):
	puzzle_in = increase('hepxxyzz')
	while True:
		flag = is_valid(puzzle_in)
		if flag: return flag
		puzzle_in = increase(puzzle_in)

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
