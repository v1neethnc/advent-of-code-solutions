# Advent of Code, 2015
# Day 17: No Such Thing as Too Much
# https://adventofcode.com/2015/day/17
# https://github.com/v1neethnc/advent-of-code-solutions


from itertools import combinations

with open("2015_17.txt") as file_data:
	data = list(map(int, file_data.read().strip().split('\n')))
	part_a, part_b = 0, 0
	for bot in range(len(data)):
		cap = 0
		for v in combinations(data, bot):
			if sum(v) == 150:
				cap += 1
		part_a += cap
		if part_b == 0 and cap != 0:
			part_b = cap
	print(f"Part A: {part_a}")
	print(f"Part B: {part_b}")