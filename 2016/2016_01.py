# Advent of Code, 2016
# Day 1: No Time for a Taxicab
# https://adventofcode.com/2016/day/1
# https://github.com/v1neethnc/advent-of-code-solutions


def movement(instructions, part = 'a'):
	directions = {'N': {'L': 'W', 'R': 'E'}, 'S': {'R': 'W', 'L': 'E'}, 'E': {'L': 'N', 'R': 'S'}, 'W': {'R': 'N', 'L': 'S'}}
	coords = {'N': [0, 1], 'S': [0, -1], 'E': [1, 0], 'W': [-1, 0]}
	start, new_dir = [0, 0], 'N'
	visited = [start]
	for i, j in instructions:
		new_dir = directions[new_dir][i]
		for _ in range(j):
			start = [start[0] + coords[new_dir][0], start[1] + coords[new_dir][1]]
			if part == 'b' and start in visited:
				return abs(start[0]) + abs(start[1])
			visited.append(start)
	if part == 'a':
		return abs(start[0]) + abs(start[1])

with open("2016_01.txt") as file_data:
	data = [[i[0], int(i[1:])] for i in file_data.read().split(', ')]
	print(f"Part A: {movement(data, 'a')}")
	print(f"Part B: {movement(data, 'b')}")
