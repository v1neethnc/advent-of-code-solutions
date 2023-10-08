# Advent of Code, 2015
# Day 21: RPG Simulator 20XX
# https://adventofcode.com/2015/day/21
# https://github.com/v1neethnc/advent-of-code-solutions


from itertools import combinations

def fight_sim(player_stats, boss_stats):
	while True:
		boss_stats[0] = boss_stats[0] - max(player_stats[1] - boss_stats[2], 1)
		if boss_stats[0] <= 0:
			return True
		player_stats[0] = player_stats[0] - max(boss_stats[1] - player_stats[2], 1)
		if player_stats[0] <= 0:
			return False

with open("2015_21.txt") as file_data:
	boss_hp = int(file_data.readline().split(": ")[1])
	damage = int(file_data.readline().split(": ")[1])
	armr = int(file_data.readline().split(": ")[1])
	
	weapons = [[8,4,0], [10,5,0], [25,6,0], [40,7,0], [74,8,0]]
	armors = [[0,0,0,], [13,0,1], [31,0,2], [53,0,3], [75,0,4], [102,0,5]]
	rings = [[0,0,0,], [25,1,0], [50,2,0], [100,3,0], [20,0,1], [40,0,2], [80,0,3]]
	player_hp = 100

	part_a = 2**32
	part_b = -1
	for weapon in weapons:
		for armor in armors:
			for ring1, ring2 in combinations(rings, 2):
				player_stats = [player_hp, weapon[1]+ring1[1]+ring2[1],armor[2]+ring1[2]+ring2[2]]
				boss_stats = [boss_hp, damage, armr]
				if fight_sim(player_stats, boss_stats):
					part_a = min(part_a, weapon[0]+armor[0]+ring1[0]+ring2[0])
				else:	
					part_b = max(part_b, weapon[0]+armor[0]+ring1[0]+ring2[0])
	
	print(f"Part A: {part_a}")
	print(f"Part B: {part_b}")