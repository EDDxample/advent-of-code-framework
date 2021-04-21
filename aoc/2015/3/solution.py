from collections import defaultdict

def move(char, x, z):
	if   char == '<': x -= 1
	elif char == '>': x += 1
	elif char == '^': z += 1
	elif char == 'v': z -= 1
	return x, z

def part1(puzzle_in: str):
	houses = defaultdict(int)
	house_count = 1
	x, z = 0, 0
	houses[(x, z)] += 1
	for char in puzzle_in:
		x, z = move(char, x, z)
		
		houses[(x, z)] += 1		
		if houses[(x, z)] == 1:
			house_count += 1

	return house_count

def part2(puzzle_in: str):
	houses = defaultdict(int)
	house_count = 1
	santa_x, santa_z = 0, 0
	rsanta_x, rsanta_z = 0, 0
	
	houses[(santa_x, santa_z)] += 1
	houses[(rsanta_x, rsanta_z)] += 1

	for i in range(0, len(puzzle_in), 2):
		charA, charB = puzzle_in[i:i+2]
		
		santa_x, santa_z = move(charA, santa_x, santa_z)
		houses[(santa_x, santa_z)] += 1

		if houses[(santa_x, santa_z)] == 1:
			house_count += 1


		rsanta_x, rsanta_z = move(charB, rsanta_x, rsanta_z)
		houses[(rsanta_x, rsanta_z)] += 1

		if houses[(rsanta_x, rsanta_z)] == 1:
			house_count += 1

	return house_count


def faster_part1(puzzle_in: str):
	houses = set()
	houses.add((0,0))

	x, z = 0, 0
	for char in puzzle_in:
		x, z = move(char, x, z)
		houses.add((x,z))
	return len(houses)

def faster_part2(puzzle_in: str):
	houses = set()
	houses.add((0,0))

	santa_x, santa_z = 0, 0
	rsanta_x, rsanta_z = 0, 0
	for i in range(0, len(puzzle_in), 2):
		char = puzzle_in[i]
		santa_x, santa_z = move(char, santa_x, santa_z)
		houses.add((santa_x, santa_z))

		char = puzzle_in[i+1]
		rsanta_x, rsanta_z = move(char, rsanta_x, rsanta_z)
		houses.add((rsanta_x, rsanta_z))

	return len(houses)
