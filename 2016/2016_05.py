# Advent of Code, 2016
# Day 5: How About a Nice Game of Chess?
# https://adventofcode.com/2016/day/5
# https://github.com/v1neethnc/advent-of-code-solutions


from hashlib import md5

def password_generator(door_id):
	part_a = ''
	ind = 0
	part_b = ['-']*8
	while len(part_a) < 8 or '-' in part_b:
		temp = door_id + str(ind)
		hash_val = md5()
		hash_val.update(temp.encode('utf-8'))
		hex_val = hash_val.hexdigest()
		if hex_val[:5] == '00000':
			if len(part_a) < 8:
				part_a += hex_val[5]
			if hex_val[5].isdigit() and int(hex_val[5]) < 8 and part_b[int(hex_val[5])] == '-':
				part_b[int(hex_val[5])] = hex_val[6]
		ind += 1
	return part_a, ''.join(part_b)

door_id = open("2016_05.txt").read()
part_a, part_b = password_generator(door_id)
print(f"Part A: {part_a}")
print(f"Part A: {part_b}")