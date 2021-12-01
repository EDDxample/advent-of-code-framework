import re
from collections import defaultdict

def part1(puzzle_in: str):
	board = defaultdict(int)	
	for claim in puzzle_in.splitlines():
		_, x, y, w, h = list(map(int, re.match(r'#(\d+)\s@\s(\d+),(\d+): (\d+)x(\d+)', claim).groups()))
		for dx in range(w):
			for dy in range(h):
				board[(x+dx, y+dy)] += 1
	count = len(list(filter(lambda v: v > 1, board.values())))
	return count


def part2(puzzle_in: str):
	board = defaultdict(int)
	for populate in (True, False):
		
		for claim in puzzle_in.splitlines():
			id, x, y, w, h = list(map(int, re.match(r'#(\d+)\s@\s(\d+),(\d+): (\d+)x(\d+)', claim).groups()))
			is_valid = True
			for dx in range(w):
				for dy in range(h):
					if populate:
						board[(x+dx, y+dy)] += 1
					elif board[(x+dx, y+dy)] != 1:
						is_valid = False
			
			if is_valid and not populate:
				return id

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
