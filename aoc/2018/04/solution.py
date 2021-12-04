import re
from collections import defaultdict

def part1(puzzle_in: str):
	# parse input and sort by date
	mapped = list(sorted(
		map(
			lambda line: re.match(r'\[\d+-(\d+)-(\d+)\s(\d+):(\d+)\]\s(.+)', line).groups(), 
			puzzle_in.splitlines()
		), 
		key = lambda x: list(map(int, x[0:4])), # month, day, hour, minute
	))

	# add sleep ranges to every guard
	guard = None
	sleeps = defaultdict(list)
	for l in mapped:
		if l[4].startswith('Guard'):
			guard = re.match(r'Guard #(\d+) begins shift', l[4]).groups()[0]
		elif guard:
			sleeps[guard].append(int(l[3]))
	
	# find the laziest guard and its sleeptime
	laziest = [0, None]
	for guard, sleeptimes in sleeps.items():
		sleeptime = 0
		for i in range(0, len(sleeptimes), 2):
			sleeptime += sleeptimes[i+1] - sleeptimes[i]
		if sleeptime > laziest[0]:
			laziest[0] = sleeptime
			laziest[1] = guard
	
	# find the most slept minute by the laziest guard
	print(laziest)
	minutes = [0] * 60
	for i in range(0, len(sleeps[laziest[1]]), 2):
		for m in range(sleeps[laziest[1]][i], sleeps[laziest[1]][i+1]):
			minutes[m] += 1
	
	max_count = max(minutes)
	max_min = minutes.index(max_count)	
	return int(laziest[1]) * max_min

def part2(puzzle_in: str):
	# parse input and sort by date
	mapped = list(sorted(
		map(
			lambda line: re.match(r'\[\d+-(\d+)-(\d+)\s(\d+):(\d+)\]\s(.+)', line).groups(), 
			puzzle_in.splitlines()
		), 
		key = lambda x: list(map(int, x[0:4])), # month, day, hour, minute
	))

	# add sleep ranges to every guard
	guard = None
	sleeps = defaultdict(list)
	for l in mapped:
		if l[4].startswith('Guard'):
			guard = re.match(r'Guard #(\d+) begins shift', l[4]).groups()[0]
		elif guard:
			sleeps[guard].append(int(l[3]))

	best = [0, 0, None] # count, minute, guard
	for guard, sleeptimes in sleeps.items():
		minutes = [0] * 60
		for i in range(0, len(sleeptimes), 2):
			for m in range(sleeptimes[i], sleeptimes[i+1]):
				minutes[m] += 1
		
		local_max_count = max(minutes)

		if local_max_count > best[0]:
			best = [
				local_max_count,
				minutes.index(local_max_count),
				guard
			]
	return int(best[2]) * best[1]


def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
