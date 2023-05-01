# Advent of Code, 2016
# Day 8: Two-Factor Authentication
# https://adventofcode.com/2016/day/8
# https://github.com/v1neethnc/advent-of-code-solutions


from copy import deepcopy

def row_updater(grid, index, shift):
	# print('row update', index, shift)
	new_grid = deepcopy(grid)
	row_vals = [[ind, val] for ind, val in enumerate(new_grid[index])]
	for row in row_vals:
		row[0] = (row[0] + shift) % 50
		new_grid[index][row[0]] = row[1]
	return new_grid

def col_updater(grid, index, shift):
	new_grid = deepcopy(grid)
	col_vals = [[ind, val[index]] for ind, val in enumerate(new_grid)]
	for col in col_vals:
		col[0] = (col[0] + shift) % 6
		new_grid[col[0]][index] = col[1]
	return new_grid

def activate(grid, coords):
	new_grid = deepcopy(grid)
	for i in range(coords[0]):
		for j in range(coords[1]):
			new_grid[j][i] = 1
	return new_grid

data = open("2016_08.txt").read().split("\n")
grid = [[0]*50 for i in range(6)]
# for i in grid:
# 	print(i)
# print()
for i in data:
	# print(i)
	tokens = i.split(' ')
	if tokens[0] == 'rect':
		coords = list(map(int, tokens[1].split('x')))
		grid = activate(grid, coords)
	else:
		ind = int(tokens[2].split('=')[1])
		shift = int(tokens[4])
		if tokens[1] == 'row':
			grid = row_updater(grid, ind, shift)
		else:
			grid = col_updater(grid, ind, shift)
	# for i in grid:
	# 	print(i)
	# print()
print(f"Part A: {sum([sum(i) for i in grid])}")
print(f"Part B:")
for row in grid:
	print(''.join(['x' if col==1 else ' ' for col in row]))