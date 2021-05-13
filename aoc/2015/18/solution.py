import numpy as np
import matplotlib.pyplot as plt
import time
from numpy.lib.stride_tricks import as_strided


def imshow_helper(board, sleepSeconds=0.5):
    ''' helper method to display a board for short time interval 
        being lazy and using the MATLAB style API '''
    plt.imshow(board, cmap="binary", interpolation="none")
    plt.axis('off')
    time.sleep(sleepSeconds)

def get3x3(arr):
    assert all(_len>2 for _len in arr.shape)
    
    nDims = len(arr.shape)
    newShape = [_len-2 for _len in arr.shape]
    newShape.extend([3] * nDims)
    
    newStrides = arr.strides + arr.strides
    return as_strided(arr, shape=newShape, strides=newStrides)

def part1(puzzle_in: str):
	iters = 100

	# rules ---------------

	rules = np.zeros((2, 9), np.uint8)
	
	# rules if off:
	rules[0, 3] = 1

	# rules if on:
	rules[1, 2] = 1
	rules[1, 3] = 1
	
	# board ---------------

	outer = np.zeros((102, 102), np.uint8)
	board = outer[1:-1, 1:-1] # from (1,1) to (100, 100)
	
	# data ---------------
	
	for y, line in enumerate(puzzle_in.splitlines()):
		for x, char in enumerate(line):
			board[y, x] = char == '#'
	
	# game ---------------

	for i in range(iters):
		neighbors = get3x3(outer)
		neighbor_count = np.sum(neighbors, (-1, -2)) - board
		board[:] = np.where(board, rules[1, neighbor_count], rules[0, neighbor_count])
	
	return np.sum(board)

def part2(puzzle_in: str):
	iters = 100

	# rules ---------------

	rules = np.zeros((2, 9), np.uint8)
	
	# rules if off:
	rules[0, 3] = 1

	# rules if on:
	rules[1, 2] = 1
	rules[1, 3] = 1
	
	# board ---------------
	outer = np.zeros((102, 102), np.uint8)
	board = outer[1:-1, 1:-1] # from (1,1) to (100, 100)
	
	# data ---------------
	
	for y, line in enumerate(puzzle_in.splitlines()):
		for x, char in enumerate(line):
			board[y, x] = char == '#'
	board[[-1,0,-1,0],[-1,-1,0,0]] = 1
	
	# game ---------------

	for i in range(iters):
		neighbors = get3x3(outer)
		neighbor_count = np.sum(neighbors, (-1, -2)) - board
		board[:] = np.where(board, rules[1, neighbor_count], rules[0, neighbor_count])
		board[[-1,0,-1,0],[-1,-1,0,0]] = 1
	return np.sum(board)

def faster_part1(puzzle_in: str):
	raise 'not implemented yet'

def faster_part2(puzzle_in: str):
	raise 'not implemented yet'
