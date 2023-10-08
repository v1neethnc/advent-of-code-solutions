# Advent of Code, 2016
# Day 7: Internet Protocol Version 7
# https://adventofcode.com/2016/day/7
# https://github.com/v1neethnc/advent-of-code-solutions


import re

def palindrome_check(line):
	if len(line) < 4:
		return False
	ind = 0
	while ind <= len(line) - 4:
		st = line[ind:ind+4]
		if st == st[::-1] and st[0] != st[1]:
			return True
		ind += 1
	return False

def four_palindrome_check(line):
	return any(p==s and r==q and p!=q for p,q,r,s in zip(line, line[1:], line[2:], line[3:]))

def three_palindrome_check(line):
	return [q+p+q for p,q,r in zip(line, line[1:], line[2:]) if p==r and p!=q]

part_a = 0
part_b = 0
data = open("2016_07.txt").read().split('\n')
for line in data:
	vals = re.findall(r"\[\w+\]", line)
	flags = [palindrome_check(vl[1:-1]) for vl in vals]
	for i in vals:
		line = line.replace(i, ' ')
	if True not in flags:		
		if four_palindrome_check(line):
			part_a += 1
	vals = ' '.join([vl[1:-1] for vl in vals])
	if any(i in vals for i in three_palindrome_check(line)):
		part_b += 1
print(f"Part A: {part_a}")
print(f"Part B: {part_b}")