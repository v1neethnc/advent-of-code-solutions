# Advent of Code, 2016
# Day 2: Bathroom Security
# https://adventofcode.com/2016/day/2
# https://github.com/v1neethnc/advent-of-code-solutions


def movement(pattern, instructions, start, part = 'a'):
	directions = {'U': [-1, 0], 'D': [1, 0], 'L': [0, -1], 'R': [0, 1]}
	for i in instructions:
		if pattern[start[0] + directions[i][0]][start[1] + directions[i][1]] != 0:
			start = [start[0] + directions[i][0], start[1] + directions[i][1]]
	return pattern[start[0]][start[1]]

def coords_converter(pattern, value):
	for ind, val in enumerate(pattern):
		if value in val:
			return [ind, val.index(value)]

with open("2016_02.txt") as file_data:
	data = [i.strip() for i in file_data.readlines()]
	pattern_a = [
		[0,0,0,0,0],
		[0,1,2,3,0],
		[0,4,5,6,0],
		[0,7,8,9,0],
		[0,0,0,0,0]
	]
	pattern_b = [
		[0,0,0,0,0,0,0],
		[0,0,0,1,0,0,0],
		[0,0,2,3,4,0,0],
		[0,5,6,7,8,9,0],
		[0,0,'A','B','C',0,0],
		[0,0,0,'D',0,0,0],
		[0,0,0,0,0,0,0]
	] 
	res = [2, 2]
	print("Part A: ", end='')
	for i in data:
		val = movement(pattern_a, i, res, 'a')
		print(val, end = '')
		res = coords_converter(pattern_a, val)
	print('\nPart B: ', end='')
	res = [2, 2]
	for i in data:
		val = movement(pattern_b, i, res, 'b')
		print(val, end = '')
		res = coords_converter(pattern_b, val)
	print()