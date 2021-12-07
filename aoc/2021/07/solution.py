import re, statistics, math

def part1(s: str, ex: str):
	# s = ex # example mode
	s = [int(x) for x in s.split(',')]
	med = statistics.median(s)

	return int(sum([abs(med - x) for x in s]))

def part2(s: str, ex: str):
	# s = ex # example mode
	s = [int(x) for x in s.split(',')]
	med = math.floor(statistics.mean(s))
	get_cost = lambda x, y: abs(y - x) * (abs(y - x) + 1) / 2
	return int(sum([get_cost(med, x) for x in s]))

def faster_part1(s: str, ex: str):
	raise 'not implemented yet'

def faster_part2(s: str, ex: str):
	raise 'not implemented yet'
