# Advent of Code, 2015
# Day 23: Opening the Turing Lock
# https://adventofcode.com/2015/day/23
# https://github.com/v1neethnc/advent-of-code-solutions


def execute_program(data, vals):
	curr = 0
	while curr < len(data):
		if data[curr][0] == 'jio':
			if vals[data[curr][-2]] == 1:
				curr += data[curr][-1]
			else:
				curr += 1
		elif data[curr][0] == 'inc':
			vals[data[curr][-1]] += 1
			curr += 1
		elif data[curr][0] == 'hlf':
			vals[data[curr][-1]] //= 2
			curr += 1
		elif data[curr][0] == 'tpl':
			vals[data[curr][-1]] *= 3
			curr += 1
		elif data[curr][0] == 'jmp':
			curr += data[curr][-1]
		elif data[curr][0] == 'jie':
			if vals[data[curr][-2]] % 2 == 0:
				curr += data[curr][-1]
			else:
				curr += 1
	return vals['b']

with open('2015_23.txt') as file:
	data = file.readlines()
	data = [i.replace(',', '').replace('+','').strip().split(' ') for i in data]
	for ind, val in enumerate(data):
		if len(val) == 3 or val[0] == 'jmp':
			data[ind][-1] = int(data[ind][-1])
	vals = {'a': 0, 'b': 0}
	print("Part A:", execute_program(data, vals))
	vals = {'a': 1, 'b': 0}
	print("Part B:", execute_program(data, vals))