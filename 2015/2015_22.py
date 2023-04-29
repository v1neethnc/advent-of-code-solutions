# Advent of Code, 2015
# Day 22: Wizard Simulator 20XX
# https://adventofcode.com/2015/day/22
# https://github.com/v1neethnc/advent-of-code-solutions


from copy import deepcopy

min_mana = 2**32
def fight_sim(playerHP, mana, bossHP, damage, activespells, is_player_turn, manaUsed, part):

	armor = 0
	if part == 'b' and is_player_turn:
		playerHP -= 1
		if playerHP < 1:
			return False
	
	new_spells = []
	for spell in activespells:
		if spell[5] >= 0:
			bossHP -= spell[1]
			playerHP += spell[2]
			armor += spell[3]
			mana += spell[4]
		if spell[5] > 1:
			new_spells.append([spell[0], spell[1], spell[2], spell[3], spell[4], spell[5]-1, spell[6]])
	
	if bossHP < 1:
		global min_mana
		if manaUsed < min_mana:
			min_mana = manaUsed
		return True

	if manaUsed >= min_mana:
		return False

	if is_player_turn:
		for spell in spells:
			is_active = False
			for t in new_spells:
				if t[-1] == spell[-1]:
					is_active = True
					break
			if mana >= spell[0] and not is_active:
				splls = deepcopy(new_spells)
				splls.append(spell)
				fight_sim(playerHP, mana - spell[0], bossHP, damage, splls, False, manaUsed + spell[0], part)
	else:
		playerHP += armor - damage if armor - damage < 0 else -1
		if playerHP > 0:
			fight_sim(playerHP, mana, bossHP, damage, new_spells, True, manaUsed, part)

spells = [
	[53,4,0,0,0,0,0],
	[73,2,2,0,0,0,1], 
	[113,0,0,7,0,6,2],
	[173,3,0,0,0,6,3],
	[229,0,0,0,101,5,4]
	]
with open("2015_22.txt") as file_data:
	bossHP = int(file_data.readline().split(": ")[1])
	damage = int(file_data.readline().split(": ")[1])
	print(bossHP, damage)
	fight_sim(50, 500, bossHP, damage, [], True, 0, 'a')
	print(f"Part A: {min_mana}")
	min_mana = 2**32
	fight_sim(50, 500, bossHP, damage, [], True, 0, 'b')
	print(f"Part B: {min_mana}")