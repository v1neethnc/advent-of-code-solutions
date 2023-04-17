# Advent of Code, 2015
# Day 4: The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4
# https://github.com/v1neethnc/advent-of-code-solutions

from hashlib import md5

def checker(part = 'a'):
	with open("2015_04.txt", encoding='utf-8') as file_data:
		data = file_data.read()
		ind = 0
		while True:
			hash_val = md5()
			temp = data + str(ind)
			hash_val.update(temp.encode())
			if part == 'a' and hash_val.hexdigest()[:5] == '00000':
				return ind
			elif part == 'b' and hash_val.hexdigest()[:6] == '000000':
				return ind
			ind += 1

# Find minimum number for which hexdigest starts with 00000
print(f"Part A: {checker('a')}")
# Find minimum number for which hexdigest starts with 000000
print(f"Part B: {checker('b')}")