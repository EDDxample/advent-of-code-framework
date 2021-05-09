import re

pattern = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')

def part1(puzzle_in: str):
	TARGET = 2503
# 	puzzle_in = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
	longest_distance = 0
	for line in re.findall(pattern, puzzle_in):
		deer, speed, sprint_duration, rest = line
		speed, sprint_duration, rest = int(speed), int(sprint_duration), int(rest)
		cycle_duration = sprint_duration + rest


		cycles = TARGET // cycle_duration
		last_section = TARGET - cycle_duration * cycles
		distance = speed * (sprint_duration * cycles + min(sprint_duration, last_section))
		# print(cycle_duration)
		# print(cycle_duration * cycles)
		# print(f'{deer} takes {TARGET / cycle_duration} cycles to run {distance}m')
		# print()
		
		longest_distance = max(longest_distance, distance)
	return longest_distance

def part2(puzzle_in: str):
	# [ { name, speed, speed, sprint_duration, rest, points } ]
# 	puzzle_in = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
	TARGET = 2503
	deers = []
	for line in re.findall(pattern, puzzle_in):
		name, speed, sprint_duration, rest = line
		deers.append({
			"name": name,
			"speed": int(speed),
			"sprint_duration": int(sprint_duration),
			"rest": int(rest),
			"points": 0,
			"distance": 0,
			"cycle_step": 0,
		})
	
	for step in range(TARGET):
		for deer in deers:
			if deer['cycle_step'] < deer['sprint_duration']:
				deer['distance'] += deer['speed']

			deer['cycle_step'] = (deer['cycle_step'] + 1) % (deer['sprint_duration'] + deer['rest'])


		# this step's winner:
		winner_ids, winner_distance = [], 0
		for i, deer in enumerate(deers):
			if winner_distance < deer['distance']:
				winner_distance = deer['distance']
				winner_ids = [i]
			elif winner_distance == deer['distance']:
				winner_ids.append(i)
		
		for deerid in winner_ids:
			deers[deerid]['points'] += 1

	winner_pts = 0
	for deer in deers:
		winner_pts = max(winner_pts, deer['points'])

	return winner_pts

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
