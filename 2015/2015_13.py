# Advent of Code, 2015
# Day 13: Knights of the Dinner Table
# https://adventofcode.com/2015/day/13
# https://github.com/v1neethnc/advent-of-code-solutions


from itertools import permutations

def happiness_calc(people_dict):
	people = set(people_dict.keys())
	max_happiness = -1
	# Permutations of people and calculate the happiness in each case
	for vals in permutations(people):
		happiness = people_dict[vals[0]][vals[-1]] + people_dict[vals[-1]][vals[0]]
		for ind in range(len(vals)-1):
			happiness += people_dict[vals[ind]][vals[ind+1]] + people_dict[vals[ind+1]][vals[ind]]
		max_happiness = max(max_happiness, happiness)
	return max_happiness

with open("2015_13.txt") as file_data:
	data = [i.strip().replace('.','').split(' ') for i in file_data.readlines()]
	ppl_dict = {}
	for i in data:
		vl = int(i[3]) if i[2] == 'gain' else -int(i[3])
		if i[0] not in ppl_dict.keys():
			ppl_dict[i[0]] = {i[-1]: vl}
		else:
			ppl_dict[i[0]][i[-1]] = vl
	print(f"Part A: {happiness_calc(ppl_dict)}")
	# Update dictionary with me in it
	ppl_dict["Me"] = {}
	for people in ppl_dict.keys():
		if people != 'Me':
			ppl_dict['Me'][people] = 0
			ppl_dict[people]['Me'] = 0
	print(f"Part B: {happiness_calc(ppl_dict)}")