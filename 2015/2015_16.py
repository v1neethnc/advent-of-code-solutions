# Advent of Code, 2015
# Day 16: Aunt Sue
# https://adventofcode.com/2015/day/16
# https://github.com/v1neethnc/advent-of-code-solutions


import re

with open("2015_16.txt") as file_data:
	data = file_data.read()
	sue_dict = {}
	for sue, k1, v1, k2, v2, k3, v3  in re.findall(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)", data):
		sue_dict[int(sue)] = {k1: int(v1), k2: int(v2), k3: int(v3)}
	mfcsam_output = {
		"children": 3,
		"cats": 7, 
		"samoyeds": 2,
		"pomeranians": 3,
		"akitas": 0,
		"vizslas": 0,
		"goldfish": 5,
		"trees": 3,
		"cars": 2,
		"perfumes": 1
	}
	# Storing Part A Sue to filter out in Part B
	part_a = None
	for sue in sue_dict.keys():
		ctr = 0
		for k in sue_dict[sue].keys():
			if sue_dict[sue][k] == mfcsam_output[k]:
				ctr += 1
		if ctr == 3:
			print(f"Part A: {sue}")
			part_a = sue
			break
	
	for sue in sue_dict.keys():
		ctr = 0
		for k in sue_dict[sue].keys():
			# Conditions needed to consider a Sue
			condition1 = k in ['cats', 'trees'] and sue_dict[sue][k] > mfcsam_output[k]
			condition2 = k in ['pomeranians', 'goldfish'] and sue_dict[sue][k] < mfcsam_output[k]
			condition3 = sue_dict[sue][k] == mfcsam_output[k]
			if condition1 or condition2 or condition3:
				ctr += 1
		if ctr == 3 and sue != part_a:
			print(f"Part B: {sue}")
			break