# Advent of Code, 2016
# Day 4: Security Through Obscurity
# https://adventofcode.com/2016/day/3
# https://github.com/v1neethnc/advent-of-code-solutions


import re

def validity_checker(room, checksum, sec_code):
	count_map = {i: room.count(i) for i in room}
	ct_map = sorted(count_map.items(), key=lambda x: (-x[1], x[0]))
	for i, j in zip(checksum, ct_map):
		if i != j[0]:
			return 0
	return sec_code

def caesar_converter(room, sec_code):
	res = ''
	for i in room:
		res += chr((ord(i) - ord('a') + sec_code%26)%26 + ord('a'))
	if 'north' in res:
		return sec_code
	return -1

part_b_flag = False
part_a = 0
part_b = 0
for line in open("2016_04.txt").readlines():
	chksum = re.findall(r"\[\w+\]", line.strip())[0]
	line = line.strip().replace(chksum, '')
	chksum = chksum[1:len(chksum)-1]
	code = re.findall(r"\d+", line.strip())[0]
	line = line.strip().replace('-' + code, '').replace('-', '')
	val = validity_checker(line, chksum, int(code))
	part_a += val
	vl = caesar_converter(line, int(code))
	if vl != -1 and not part_b_flag:
		part_b = vl
print(f"Part A: {part_a}")
print(f"Part B: {part_b}")