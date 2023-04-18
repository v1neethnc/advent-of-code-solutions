# Advent of Code, 2015
# Day 6: Probably a Fire Hazard
# https://adventofcode.com/2015/day/6
# https://github.com/v1neethnc/advent-of-code-solutions

def grid_updater(grid_state, instruction, part = 'a'):
	start, end = instruction[1], instruction[2]
	inst_a = {'on': 1, 'off': 0}
	inst_b = {'on': 1, 'off': -1}
	if instruction[0] in ['on', 'off']:
		for row in range(start[0], end[0]+1):
			for col in range(start[1], end[1]+1):
				# Update the grid for Part A by simply switching on or off
				if part == 'a':
					grid_state[row][col] = inst_a[instruction[0]]
				# Update the grid for Part B by changing brightness and limiting min to 0
				else:
					grid_state[row][col] += inst_b[instruction[0]]
					grid_state[row][col] = max(grid_state[row][col], 0)
	else:
		for row in range(start[0], end[0]+1):
			for col in range(start[1], end[1]+1):
				# Update the grid for Part A by toggling on or off
				if part == 'a':
					grid_state[row][col] = 0 if grid_state[row][col] == 1 else 1
				# Update the grid for Part B by increasing brightness by 2
				else:
					grid_state[row][col] += 2
	return grid_state

with open("2015_06.txt") as file_data:
	data = [i.strip().replace('turn ', '').replace('through ', '').split(' ') for i in file_data.readlines()]
	for ind in range(len(data)):
		data[ind][1] = list(map(int, data[ind][1].split(',')))
		data[ind][2] = list(map(int, data[ind][2].split(',')))

grid_a = [[0 for j in range(1000)] for i in range(1000)]
grid_b = [[0 for j in range(1000)] for i in range(1000)]
for ins in data:
	grid_a = grid_updater(grid_a, ins, 'a')
	grid_b = grid_updater(grid_b, ins, 'b')

part_a, part_b = 0, 0
for row1, row2 in zip(grid_a, grid_b):
	part_a += sum(row1)
	part_b += sum(row2)
print(f"Part A: {part_a}")
print(f"Part B: {part_b}")