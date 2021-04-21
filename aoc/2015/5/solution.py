from collections import Counter

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

def part1(puzzle_in: str):
	count = 0
	for line in puzzle_in.splitlines():
		if is_nice(line): count += 1
	return count

def part2(puzzle_in: str):
	return 'not implemented yet'

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
