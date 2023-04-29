# Advent of Code, 2015
# Day 24: It Hangs in the Balance
# https://adventofcode.com/2015/day/24
# https://github.com/v1neethnc/advent-of-code-solutions


from itertools import combinations
from functools import reduce
from operator import mul
def entanglement_checker(data, groups):
	size = sum(data) // groups
	for i in range(len(data)):
		vals = [reduce(mul, comb) for comb in combinations(data, i) if sum(comb) == size]
		if len(vals) > 0:
			return min(vals)


with open("2015_24.txt") as file_data:
	data = [int(i.strip()) for i in file_data.readlines()]

	print(f"Part A: {entanglement_checker(data, 3)}")
	print(f"Part B: {entanglement_checker(data, 4)}")