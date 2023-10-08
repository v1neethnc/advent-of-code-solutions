# Advent of Code, 2015
# Day 8: Matchsticks
# https://adventofcode.com/2015/day/8
# https://github.com/v1neethnc/advent-of-code-solutions


with open("2015_08.txt") as file_data:
    data = [i.strip() for i in file_data.readlines()]
    # Using eval() function to evaluate the string
    part_a = sum([len(i) - len(eval(i)) for i in data])
    print(f"Part A: {part_a}")
    # After removing the original string, the result is
	# the number of double quotes and backslashes + 2 (starting and end quotes)
    part_b = sum([i.count('"') + i.count('\\') + 2 for i in data])
    print(f"Part B: {part_b}")