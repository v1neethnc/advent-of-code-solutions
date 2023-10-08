# Advent of Code, 2015
# Day 11: Corporate Policy
# https://adventofcode.com/2015/day/11
# https://github.com/v1neethnc/advent-of-code-solutions


def password_updater(passwrd):
	all_poss_vals = [chr(i)*2 + chr(i+1) + chr(i+2)*2 for i in range(ord('a'), ord('y'))]
	all_poss_vals = [[j for j in i] for i in all_poss_vals if 'i' not in i and 'o' not in i and 'l' not in i]

	pass_substr = [i for i in passwrd[-5:]]
	for vals in all_poss_vals:
		res_ind, flag = -1, False
		for v1, v2 in zip(pass_substr, vals):
			if v1 == v2:
				continue
			if v1 < v2:
				res_ind = all_poss_vals.index(vals)
				break
			elif v1 > v2:
				flag = True
				res_ind = (all_poss_vals.index(vals) + 1) % len(all_poss_vals)
				break
		if res_ind == -1:
			flag = True
			res_ind = (all_poss_vals.index(vals) + 1) % len(all_poss_vals)
			break
	start = passwrd[:-5]
	if flag:
		start, ind = '', -6
		while ind >= -len(passwrd):
			prev = chr((ord(passwrd[ind]) + 1 - ord('a')) % 26 + ord('a'))
			start = prev + start
			if prev != 'a':
				start = passwrd[:ind] + start
				break
	return start + ''.join(all_poss_vals[res_ind])

part_a = password_updater('cqjxjnds')
print(f"Part A: {part_a}")
print(f"Part B: {password_updater(part_a)}")