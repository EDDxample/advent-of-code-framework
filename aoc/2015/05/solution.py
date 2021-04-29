from collections import Counter
import re

banlist = { 'a':'b', 'c':'d', 'p':'q', 'x':'y' }

def is_nice(string):
	global banlist
	chars = Counter(string)
	
	# 3 vowels
	if chars['a'] + chars['e'] + chars['i'] + chars['o'] + chars['u'] < 3:
		return False

	# repeated letter
	repeated_letter_flag = False
	
	for i in range(len(string) - 1):
		char = string[i]
		
		if char == string[i+1]:
			repeated_letter_flag = True
		
		# has not ab, cd, pq, or xy
		if char in banlist and string[i+1] == banlist[char]:
			return False
	
	return repeated_letter_flag

has_repeated_pair = re.compile(r'(\w\w).*\1')
has_xyx = re.compile(r'(\w).\1')

def is_nice2(string: str):
	global has_repeated_pair, has_xyx
	return re.search(has_repeated_pair, string) and re.search(has_xyx, string)

def part1(puzzle_in: str):
	count = 0
	for line in puzzle_in.splitlines():
		if is_nice(line): count += 1
	return count

def part2(puzzle_in: str):
	count = 0
	for line in puzzle_in.splitlines():
		if is_nice2(line): count += 1
	return count

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
