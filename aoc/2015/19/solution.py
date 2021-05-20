from collections import defaultdict
from random import shuffle
import re

pattern = re.compile(r'(\w+) => (\w+)')

def replace_string(string, key, val, pos):
	return string[:pos] + val + string[pos + len(key):]

def get_pattern_locations(dna, pattern):
	try:
		pos = dna.index(pattern, 0)
		while True:
			yield pos
			pos = dna.index(pattern, pos + 1)
	except ValueError: pass

def part1(puzzle_in: str):
	flag = False
	rules = defaultdict(list)
	dna = ''
	
	molecules = set()
	
	# parse input ==================

	for line in puzzle_in.splitlines():
		if line == '':
			flag = True

		elif flag:
			dna = line

		else:
			match = pattern.match(line)
			rules[match[1]].append(match[2])

	# apply rules ===============

	for key, vals in rules.items():
		for pos in get_pattern_locations(dna, key):
			for val in vals:
				molecules.add(replace_string(dna, key, val, pos))
		
	return len(molecules)

def part2(puzzle_in: str):
	flag = False
	rules = defaultdict(list)
	dna = ''
	
	molecules = set()
	
	# parse input ==================

	for line in puzzle_in.splitlines():
		if line == '':
			flag = True

		elif flag:
			dna = line

		else:
			match = pattern.match(line)
			rules[match[2]].append(match[1])

	# solution ===============
	
	target = dna
	steps = 0

	while target != 'e':
		tmp = target
		for key, vals in rules.items():
			if key not in target: continue

			for val in vals:
				target = target.replace(key, val, 1)
				steps += 1
		if tmp == target:
			target = dna
			steps = 0
			shuffle(rules) # wtf...
	return steps


def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
