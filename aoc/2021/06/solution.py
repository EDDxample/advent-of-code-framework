import re
from collections import Counter, defaultdict

def part1(s: str, ex: str):
	# new born: 2 days to adult -> timer 8
	# adult: 7 days to reproduce -> 

	# s = ex # example mode
	s = [int(n) for n in s.split(',')]

	fish_count = Counter(s)
	for day in range(80):
		new_count = defaultdict(int)
		for i in range(9):
			if i == 0:
				new_count[6] += fish_count[i]
				new_count[8] += fish_count[i]
			else:
				new_count[i-1] += fish_count[i]
		fish_count = new_count
		# print([x for k, v in fish_count.items() for x in [k] * v if v])
	return sum(fish_count.values())

def part2(s: str, ex: str):
	# new born: 2 days to adult -> timer 8
	# adult: 7 days to reproduce -> 

	# s = ex # example mode
	s = [int(n) for n in s.split(',')]

	fish_count = Counter(s)
	for day in range(256):
		new_count = defaultdict(int)
		for i in range(9):
			if i == 0:
				new_count[6] += fish_count[i]
				new_count[8] += fish_count[i]
			else:
				new_count[i-1] += fish_count[i]
		fish_count = new_count
		# print([x for k, v in fish_count.items() for x in [k] * v if v])
	return sum(fish_count.values())

def faster_part1(s: str, ex: str):
	raise 'not implemented yet'

def faster_part2(s: str, ex: str):
	raise 'not implemented yet'
