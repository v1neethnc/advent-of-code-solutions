# Advent of Code, 2015
# Day 2: I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2
# https://github.com/v1neethnc/advent-of-code-solutions

def area_calc(l, b, h):
	return 2*(l*b + b*h + h*l) + l*b

def ribbon_calc(l, b, h):
	return l*b*h + 2*(l+b)

with open("2015_02.txt") as file_data:
	data = [list(map(int, i.strip().split('x'))) for i in file_data.readlines()]
	part_a, part_b = 0, 0
	for val in data:
		val.sort()
		part_a += area_calc(val[0], val[1], val[2])
		part_b += ribbon_calc(val[0], val[1], val[2])

	# Part A calculates the total area of paper required
	print(f"Part A: {part_a}")
	# Part B calculates the total ribbon needed
	print(f"Part B: {part_b}")