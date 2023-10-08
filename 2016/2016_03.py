# Advent of Code, 2016
# Day 3: Squares With Three Sides
# https://adventofcode.com/2016/day/3
# https://github.com/v1neethnc/advent-of-code-solutions


import re

def triangle_checker(sides):
	cond1 = sides[0]+sides[1] > sides[2]
	cond2 = sides[1]+sides[2] > sides[0]
	cond3 = sides[2]+sides[0] > sides[1]
	return cond1 and cond2 and cond3

def triangle_counter(dt):
	ctr = 0
	for i in dt:
		if triangle_checker(i):
			ctr += 1
	return ctr

data = [int(i) for i in re.findall(r"\d+", open("2016_03.txt").read())]
dt = [data[i:i+3] for i in range(0, len(data), 3)]
print(f"Part A: {triangle_counter(dt)}")
dt = [data[j:j+7:3] for i in range(0, len(data), 9) for j in range(i, i+3)]
print(f"Part B: {triangle_counter(dt)}")
