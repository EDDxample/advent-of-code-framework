import re, string
from typing import List

def part1(s: str, ex: str):
	
	# s = ex # example mode
	s = s[:-1]
	return react(s)


def part2(s: str, ex: str):
		
	# s = ex # example mode
	s = s[:-1]
	
	keys = set([c.lower() for c in s])

	return min([react(s.replace(k, '').replace(k.upper(), '')) for k in keys])

def faster_part1(s: str, ex: str):
	raise 'not implemented yet'

def faster_part2(s: str, ex: str):
	raise 'not implemented yet'

def react(s: str):
	buf: List[str] = []
	for c in s:
		if buf and c == buf[-1].swapcase():
			buf.pop()
		else:
			buf.append(c)
	return len(buf)