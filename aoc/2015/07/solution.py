# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i


def part1(puzzle_in: str):
	variables = {}
	pending = {}

	for line in puzzle_in.splitlines():
		operation, out = line.split(' -> ')
		pending[out.strip()] = operation.strip().split(' ')

	def get(target):
		# return if constant
		try: return int(target)
		except: pass

		if target not in variables:
			params = pending[target]

			if len(params) == 1: # assign
				out = get(params[0])
			else:
				operation = params[-2]
				out = {
					'NOT':    lambda: ~get(params[1]),
					'OR':     lambda:  get(params[0]) | get(params[2]),
					'AND':    lambda:  get(params[0]) & get(params[2]),
					'RSHIFT': lambda:  get(params[0]) >> get(params[2]),
					'LSHIFT': lambda:  get(params[0]) << get(params[2]),
				}[operation]()
			variables[target] = out
		return variables[target]
	return get('a')



	return 'not implemented yet'

def part2(puzzle_in: str):
	variables = {}
	pending = {}

	for line in puzzle_in.splitlines():
		operation, out = line.split(' -> ')
		pending[out.strip()] = operation.strip().split(' ')

	def get(target):
		# return if constant
		try: return int(target)
		except: pass

		if target not in variables:
			params = pending[target]

			if len(params) == 1: # assign
				out = 956 if target == 'b' else get(params[0])
			else:
				operation = params[-2]
				out = {
					'NOT':    lambda: ~get(params[1]),
					'OR':     lambda:  get(params[0]) | get(params[2]),
					'AND':    lambda:  get(params[0]) & get(params[2]),
					'RSHIFT': lambda:  get(params[0]) >> get(params[2]),
					'LSHIFT': lambda:  get(params[0]) << get(params[2]),
				}[operation]()
			variables[target] = out
		return variables[target]
	return get('a')

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'