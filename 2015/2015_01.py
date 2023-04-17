# Advent of Code, 2015
# Day 1: Not Quite Lisp
# https://adventofcode.com/2015/day/1
# https://github.com/v1neethnc/advent-of-code-solutions

def parser(part = 'a'):
	with open("2015_01.txt") as file_data:
		data = file_data.read()
		flr = 0
		for ind, val in enumerate(data):
			if val == '(':
				flr += 1
			else:
				flr -= 1
			if part == 'b' and flr == -1:
				return ind
	return flr

# Part A returns the floor
print(f"Part A: {parser('a')}")
# Part B returns the index where floor is -1
print(f"Part B: {parser('b')}")