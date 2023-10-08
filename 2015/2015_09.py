# Advent of Code, 2015
# Day 9: All in a Single Night
# https://adventofcode.com/2015/day/9
# https://github.com/v1neethnc/advent-of-code-solutions


from itertools import permutations

stars, dists = set(), dict()
with open('2015_09.txt') as file_data:
	for i in file_data.readlines():
		vals = i.split()
		stars.add(vals[0])
		stars.add(vals[2])
		if vals[0] in dists:
			dists[vals[0]][vals[2]] = int(vals[4])
		else:
			dists[vals[0]] = {vals[2]: int(vals[4])}
		if vals[2] in dists:
			dists[vals[2]][vals[0]] = int(vals[4])
		else:
			dists[vals[2]] = {vals[0]: int(vals[4])}

part_a, part_b = 2**32, -1
for vals in permutations(stars):
	dist = 0
	for j in range(len(stars)-1):
		dist += dists[vals[j]][vals[j+1]]
	part_a = min(part_a, dist)
	part_b = max(part_b, dist)

print(f"Part A: {part_a}")
print(f"Part B: {part_b}")