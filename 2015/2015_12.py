# Advent of Code, 2015
# Day 12: JSAbacusFramework.io
# https://adventofcode.com/2015/day/12
# https://github.com/v1neethnc/advent-of-code-solutions


import re
import json

def conditional_sum(data):
	if isinstance(data, int):
		return data
	# Sum of each list element and return overall sum
	if isinstance(data, list):
		return sum([conditional_sum(i) for i in data])
	# Sum of each dict value if 'red' is not in values
	if isinstance(data, dict):
		if 'red' in data.values():
			return 0
		return sum([conditional_sum(i) for i in data.values()])
	return 0

with open('2015_12.txt') as file_data:
	data = file_data.read()
	part_a = sum([int(i) for i in re.findall(r"-{0,1}\d+", data)])
	print(part_a)
	
	data = json.loads(data)
	part_b = conditional_sum(data)
	print(part_b)