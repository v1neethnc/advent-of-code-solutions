# Advent of Code, 2015
# Day 3: Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3
# https://github.com/v1neethnc/advent-of-code-solutions


def coords_changer(coords, move):
	move_dict = {'^': [0, 1], 'v': [0, -1], '>': [1, 0], '<': [-1, 0]}
	return tuple([coords[0] + move_dict[move][0], coords[1] + move_dict[move][1]])

def moves_calc(moves):
	houses_dict = {(0, 0): 1}
	coords = (0, 0)
	for i in moves:
		coords = coords_changer(coords, i)
		if coords in houses_dict.keys():
			houses_dict[coords] += 1
		else:
			houses_dict[coords] = 1
	return houses_dict

with open("2015_03.txt") as file_data:
	data = file_data.read()

	res = moves_calc(data)
	# The houses in res are the houses with at least one present
	print(f"Part A: {len(res.keys())}")

	santa_mov = moves_calc(data[::2])
	robo_mov = moves_calc(data[1::2])

	# Getting the houses visited by Santa and Robo-Santa
	santa_mov = set(santa_mov.keys())
	robo_mov = set(robo_mov.keys())

	# The answer is union of both sets
	print(f"Part B: {len(santa_mov.union(robo_mov))}")