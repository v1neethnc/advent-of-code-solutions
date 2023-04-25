# Advent of Code, 2015
# Day 18: Like a GIF For Your Yard
# https://adventofcode.com/2015/day/18
# https://github.com/v1neethnc/advent-of-code-solutions


from copy import deepcopy

def neighbor_checker(grid, coords):
	ctr = 0
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if not (x == 0 and y == 0) and grid[coords[0]+x][coords[1]+y] == '#':
				ctr +=1
	return ctr

def grid_updater(grid, part = 'a'):
	new_grid = deepcopy(grid)
	min_v, max_v = 1, len(grid[0])-1

	for row in range(min_v, max_v):
		for col in range(min_v, max_v):
			if part == 'b' and row in [min_v, max_v-1] and col in [min_v, max_v-1]:
				continue
			on_ctr = neighbor_checker(grid, [row,col])
			if grid[row][col] == '#':
				if on_ctr not in [2, 3]:
					new_grid[row][col] = '.'
			else:
				if on_ctr == 3:
					new_grid[row][col] = '#'
	return new_grid

def grid_creator(part = 'a'):
	with open('2015_18.txt') as file_data:
		grid = []
		for line in file_data.readlines():
			line_ln = len(line.strip())
			ln = ['.'] + [i for i in line.strip()] + ['.']
			grid.append(ln)
		grid = [['.' for i in range(line_ln+2)]] + grid + [['.' for i in range(line_ln+2)]]
		if part == 'b':
			grid[1][1] = grid[1][len(grid[0])-2] = grid[len(grid[0])-2][1] = grid[len(grid[0])-2][len(grid[0])-2] = '#'
	return grid

grid = grid_creator('a')
iters = 100
for _ in range(iters):
	grid = grid_updater(grid, 'a')
part_a = sum([i.count('#') for i in grid]) 
print(f"Part A: {part_a}")
grid = grid_creator('b')
for _ in range(iters):
	grid = grid_updater(grid, 'b')
part_b = sum([i.count('#') for i in grid])
print(f"Part B: {part_b}") 