# Advent of Code, 2015
# Day 25: Let It Snow
# https://adventofcode.com/2015/day/25
# https://github.com/v1neethnc/advent-of-code-solutions


import re

def code_gen(current):
	return (current * 252533) % 33554393

def paper_filler(val, row, col):
	r, c, ind = 1, 1, 1
	while True:
		if r == 1:
			r = c + 1
			c = 1
		else:
			r -= 1
			c += 1
		val = code_gen(val)
		if [r, c] == [row, col]:
			return val

with open("2015_25.txt") as file_data:
	data = [int(i) for i in re.findall(r"(\d+)", file_data.read())]
	first = 20151125
	print("Part A: {paper_filler(first, data[0], data[1])}")