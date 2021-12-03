import re

def part1(puzzle_in: str):
	bitlen = puzzle_in.index('\n')
	cb = [0] * bitlen
	count = 0
	for line in puzzle_in.splitlines():
		count += 1
		byte = int(line, 2)
		for i in range(bitlen):
			if (byte >> (bitlen - 1 - i)) & 1:
				cb[i] += 1
	gammabits = []
	epsilonbits = []
	for bit in cb:
		flag = bit > count / 2
		gammabits.append(str(int(flag)))
		epsilonbits.append(str(int(not flag)))
	
	print('most', ''.join(gammabits))
	print('least', ''.join(epsilonbits))

	gamma = int(''.join(gammabits), 2)
	epsilon = int(''.join(epsilonbits), 2)
	return gamma * epsilon
	
def part2(puzzle_in: str):
	bitlen = puzzle_in.index('\n')
	oxys = puzzle_in.splitlines().copy()
	co2s = puzzle_in.splitlines().copy()
	
	for i in range(bitlen):
		if len(oxys) != 1:
			ones, zeros = [], []
			for s in oxys:
				if s[i] == '1':
					ones.append(s)
				else:
					zeros.append(s)
			
			if len(ones) >= len(zeros):
				oxys = ones
			else:
				oxys = zeros

		if len(co2s) != 1:
			ones, zeros = [], []
			for s in co2s:
				if s[i] == '1':
					ones.append(s)
				else:
					zeros.append(s)
			
			if len(ones) < len(zeros):
				co2s = ones
			else:
				co2s = zeros
	
	oxy = int(oxys[0], 2)
	co2 = int(co2s[0], 2)

	return oxy * co2

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
