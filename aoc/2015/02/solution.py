
def calcPaper(w,h,l):
	a, b, c = w*h, w*l, h*l
	m = min((a,b,c))
	return 2 * (a + b + c) + m

def calcRibbon(w,h,l):
	loop = w*h*l
	a, b = sorted((w,h,l))[:2]
	return 2*a + 2*b + loop

def part1(puzzle_in:str):
	total = 0
	for line in puzzle_in.split('\n'):
		try:
			w, h, l = line.split('x')
			total += calcPaper(int(w), int(h), int(l))
		except: pass
	return total

def part2(puzzle_in:str):
	total = 0
	for line in puzzle_in.split('\n'):
		try:
			w, h, l = line.split('x')
			total += calcRibbon(int(w), int(h), int(l))
		except: pass
	return total
