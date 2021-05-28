import re

pattern = re.compile(r'(\w+)\s([-+]?\w+),?\s?([-+]\w+)?[\n$]')


def part1(puzzle_in: str):
	registers = {
		'a': 0,
		'b': 0,
	}
	
	pc = 0
	lines = pattern.findall(puzzle_in)

	while pc < len(lines):
		opcode, r, offset = lines[pc]
		if offset: offset = int(offset)
		pc += 1

		if opcode == 'hlf':
			registers[r] //= 2
		elif opcode == 'tpl':
			registers[r] *= 3
		elif opcode == 'inc':
			registers[r] += 1
		elif opcode == 'jie':
			if registers[r] % 2 == 0:
				pc += offset - 1
		elif opcode == 'jio':
			if registers[r] == 1:
				pc += offset - 1
		elif opcode == 'jmp':
			pc += int(r) - 1
		else:
			print('ERROR', opcode, r, offset)
			raise Exception()

	return registers['b']

def part2(puzzle_in: str):
	registers = {
		'a': 1,
		'b': 0,
	}
	
	pc = 0
	lines = pattern.findall(puzzle_in)

	while pc < len(lines):
		opcode, r, offset = lines[pc]
		if offset: offset = int(offset)
		pc += 1

		if opcode == 'hlf':
			registers[r] //= 2
		elif opcode == 'tpl':
			registers[r] *= 3
		elif opcode == 'inc':
			registers[r] += 1
		elif opcode == 'jie':
			if registers[r] % 2 == 0:
				pc += offset - 1
		elif opcode == 'jio':
			if registers[r] == 1:
				pc += offset - 1
		elif opcode == 'jmp':
			pc += int(r) - 1
		else:
			print('ERROR', opcode, r, offset)
			raise Exception()

	return registers['b']

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
