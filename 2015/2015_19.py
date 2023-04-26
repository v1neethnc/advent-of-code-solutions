# Advent of Code, 2015
# Day 19: Medicine for Rudolph
# https://adventofcode.com/2015/day/19
# https://github.com/v1neethnc/advent-of-code-solutions


with open("2015_19.txt") as file_data:
	data = [i.strip().split(" => ") for i in file_data.readlines()]
	main_str = data[-1][0]
	data = data[:-2]
	# print(main_str)

	res = set()
	for i, j in data:
		for ind in range(len(main_str)):
			if main_str[ind:ind+len(i)] == i:
				eq_str = main_str[:ind] + j + main_str[ind+len(i):]
				res.add(eq_str)
	print(f"Part A: {len(res)}")

	# Implemented the solution found at https://reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju/
	ctr1, ctr2, ctr3 = main_str.count('Rn'), main_str.count('Ar'), main_str.count('Y')
	main_ctr = sum([main_str.count(i) for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'])
	part_b = main_ctr - (ctr1 + ctr2 + 2*ctr3 + 1)
	print(f"Part B: {part_b}")