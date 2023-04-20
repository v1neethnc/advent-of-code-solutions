# Advent of Code, 2015
# Day 14: Reindeer Olympics
# https://adventofcode.com/2015/day/14
# https://github.com/v1neethnc/advent-of-code-solutions


import re

with open('2015_14.txt') as file_data:
	data = file_data.read()
	dists = []
	for name, speed, time, rest in re.findall(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', data):
		sec_distances = [int(speed) if i%(int(time)+int(rest)) < int(time) else 0 for i in range(2503)]
		dists.append(sec_distances)
	
	print(f"Part A: {max([sum(i) for i in dists])}")
	pts = [0 for i in range(len(dists))]
	for i in range(1, len(dists[0])):
		vls = [sum(j[:i]) for j in dists]
		indices = [i for i, v in enumerate(vls) if v == max(vls)]
		for j in indices:
			pts[j] += 1
	print(f"Part B: {max(pts)}")
