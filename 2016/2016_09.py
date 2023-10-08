# Advent of Code, 2016
# Day 9: Explosives in Cyberspace
# https://adventofcode.com/2016/day/9
# https://github.com/v1neethnc/advent-of-code-solutions


import re

def decomp_len_calc(string, part='a'):
	bracket = re.search(r'\((\d+)x(\d+)\)', string)
	if not bracket:
		return len(string)
	pos, substr_size, repeat = bracket.start(0), int(bracket.group(1)), int(bracket.group(2))
	new_pos = pos + len(bracket.group())
	if part == 'a':
		return len(string[:pos]) + len(string[new_pos:new_pos+substr_size]) * repeat + decomp_len_calc(string[new_pos+substr_size:], part)
	return len(string[:pos]) + decomp_len_calc(string[new_pos:new_pos+substr_size], part) * repeat + decomp_len_calc(string[new_pos+substr_size:], part)
	
data = open("2016_09.txt").read()
print(f"Part A: {decomp_len_calc(data, 'a')}")
print(f"Part A: {decomp_len_calc(data, 'b')}")