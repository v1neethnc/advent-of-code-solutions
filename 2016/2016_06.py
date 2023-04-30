# Advent of Code, 2016
# Day 6: Signals and Noise
# https://adventofcode.com/2016/day/6
# https://github.com/v1neethnc/advent-of-code-solutions


data = open("2016_06.txt").read().split('\n')
sub_lists = [[] for i in range(len(data[0]))]
for i in data:
	for j in range(len(i)):
		sub_lists[j].append(i[j])
part_a, part_b = '', ''

for line in sub_lists:
	counter_dict = {i: line.count(i) for i in line}
	ct_map = sorted(counter_dict.items(), key=lambda x: (-x[1]))
	part_a += ct_map[0][0]
	part_b += ct_map[-1][0]

print(f"Part A: {part_a}")
print(f"Part B: {part_b}")