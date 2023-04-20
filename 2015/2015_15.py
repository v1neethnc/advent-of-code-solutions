# Advent of Code, 2015
# Day 14: Reindeer Olympics
# https://adventofcode.com/2015/day/14
# https://github.com/v1neethnc/advent-of-code-solutions


def max_score_calc(part = 'a'):
	max_val = 0
	for i in range(100):
		for j in range(100-i):
			for k in range(100-i-j):
				l = 100-(i+j+k)
				counts = [sum([ingr_scores[row][col]*mul for row, mul in zip(range(len(ingr_scores)), [i,j,k,l])]) for col in range(len(ingr_scores[0]))]
				if all(i>=0 for i in counts[:-1]):
					res = prod(counts[:-1])
				else:
					res = 0
				if part == 'b' and counts[-1] != 500:
					continue
				max_val = max(max_val, res)
	return max_val


from numpy import prod
with open('2015_15.txt') as file_data:
	data = file_data.readlines()
	ingr_scores = []
	for line in data:
		vals = line.replace(',', '').split(' ')
		ingr_scores.append(list(map(int,[vals[2], vals[4], vals[6], vals[8], vals[10]])))
	print(f"Part A: {max_score_calc('a')}")
	print(f"Part B: {max_score_calc('b')}")