# Advent of Code, 2015
# Day 20: Infinite Elves and Infinite Houses
# https://adventofcode.com/2015/day/20
# https://github.com/v1neethnc/advent-of-code-solutions


def divisor_sum(n, part = 'a'):
	if part == 'a':
		sm_set = set([1, n])
		ind = 2
		while ind <= n**0.5:
			if n % ind == 0:
				sm_set.add(ind)
				sm_set.add(n//ind)
			ind += 1
		return sum(sm_set)*10
	if part == 'b':
		sm_set = set()
		for ind in range(1, 51):
			if n%ind == 0:
				sm_set.add(n)
				sm_set.add(n//ind)
		return sum(sm_set)*11


with open("2015_20.txt") as file_data:
	min_prizes = int(file_data.read())
	ind = 2

	while True:
		prizes = divisor_sum(ind)
		if prizes >= min_prizes:
			print(f"Part A: {ind}")
			break
		ind += 1
	
	ind = 51
	while True:
		prizes = divisor_sum(ind, 'b')
		if prizes >= min_prizes:
			print(f"Part B: {ind}")
			break
		ind += 1