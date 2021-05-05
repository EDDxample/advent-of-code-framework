import re, json

num_pattern = re.compile(r'(-?\d+)')

def count_values(obj):
	count = 0
	try: count = int(obj)
	except TypeError:
		if type(obj) is list:
			for x in obj:
				count += count_values(x)

		elif type(obj) is dict:
			if 'red' in obj.values(): return 0
			for key in obj:
				count += count_values(key)
				count += count_values(obj[key])
	except ValueError: pass
	finally: return count

def part1(puzzle_in: str):
	return sum(map(int, re.findall(num_pattern, puzzle_in)))

def part2(puzzle_in: str):
	data: object = json.loads(puzzle_in)
	return count_values(data)


def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
