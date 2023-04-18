# Advent of Code, 2015
# Day 10: Elves Look, Elves Say
# https://adventofcode.com/2015/day/10
# https://github.com/v1neethnc/advent-of-code-solutions


def look_and_say(ctr, data = None, last_ctr = 0):
	# Use last known values if any
	ct_temp = last_ctr
	if data is None:
		data = open("2015_10.txt").read()
	while ct_temp < ctr:
		temp_data = ''
		val, temp_ctr, ind = data[0], 1, 1
		while ind < len(data):
			while ind < len(data) and data[ind] == val:
				temp_ctr += 1
				ind += 1
			temp_data += str(temp_ctr) + str(val)
			val = data[ind] if ind < len(data) else 0
			temp_ctr = 0
		data = temp_data
		ct_temp += 1
	return data

with open("2015_10.txt") as file_data:
	part_a = look_and_say(40)
	print(f"Part A: {len(part_a)}")
	part_b = look_and_say(50, part_a, 40)
	print(f"Part B: {len(part_b)}")