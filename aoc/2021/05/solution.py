import re
from collections import defaultdict
from itertools import product

def part1(s: str, ex: str):
	# s = ex # example mode
	
	s = s.splitlines()
	s = [
		[min(int(x1),int(x2)), min(int(y1),int(y2)), max(int(x1),int(x2)), max(int(y1),int(y2))]
		for x1, y1, x2, y2 in (re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in s)
	]
	
	coords = defaultdict(int)
	overlaps = 0
	for x1, y1, x2, y2 in s:
		if x1 == x2 or y1 == y2:
			for xy in product(range(x1, x2+1), range(y1, y2+1)):
				coords[xy] += 1
				if coords[xy] == 2:
					overlaps += 1

	return overlaps


def part2(s: str, ex: str):
	# s = ex # example mode
	
	s = s.splitlines()
	s = [
		[int(x1), int(y1), int(x2), int(y2)] for x1, y1, x2, y2 in (re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups() for line in s)
	]
	
	coords = defaultdict(int)
	overlaps = 0
	for x1, y1, x2, y2 in s:
		if x1 == x2 or y1 == y2: # horizontal or vertical
			x1, x2 = min(x1, x2), max(x1, x2)
			y1, y2 = min(y1, y2), max(y1, y2)
			
			for xy in product(range(x1, x2+1), range(y1, y2+1)):
				coords[xy] += 1
				if coords[xy] == 2:
					overlaps += 1
		
		else: # diagonals
			dx = 1 if x2 > x1 else -1
			dy = 1 if y2 > y1 else -1
			for xy in zip(range(x1, x2 + dx, dx), range(y1, y2 + dy, dy)):
				coords[xy] += 1
				if coords[xy] == 2:
					overlaps += 1

	return overlaps

def faster_part1(s: str, ex: str):
	raise 'not implemented yet'

def faster_part2(s: str, ex: str):
	raise 'not implemented yet'
