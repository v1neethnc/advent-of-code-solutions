# Advent of Code, 2015
# Day 5: Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5
# https://github.com/v1neethnc/advent-of-code-solutions

import re

def is_nice_part_a(val):
	# First search pattern: check if any of ab,ef,pq,xy are present and remove those strings
	# Second search pattern: check if any of the vowels are present three or more times
	# Third search pattern: take a character and check if it repeats again 
	return (not re.search(r"ab|ef|pq|xy", val)) and re.search(r"([aeiou].*){3,}", val) and re.search(r"(.)\1", val)

def is_nice_part_b(val):
	# First search pattern: take two characters and check if the first one repeats after the second one
	# Second search pattern: take a pair of characters and check if they repeat again in the string
	return re.search(r"(.).\1", val) and re.search(r"(..).*\1", val)

with open("2015_05.txt") as file_data:
	data = [i.strip() for i in file_data.readlines()]
	part_a, part_b = 0, 0
	for val in data:
		if is_nice_part_a(val):
			part_a += 1
		if is_nice_part_b(val):
			part_b += 1
	print(f"Part A: {part_a}")
	print(f"Part B: {part_b}")