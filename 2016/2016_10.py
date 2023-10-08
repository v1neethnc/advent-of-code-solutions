# Advent of Code, 2016
# Day 10: Balance Bots
# https://adventofcode.com/2016/day/10
# https://github.com/v1neethnc/advent-of-code-solutions

from collections import defaultdict
from copy import deepcopy
def are_all_allocated(bot_dict):
    return sum(len(val) for val in bot_dict.values()) == len(bot_dict.keys()) * 2 and len(bot_dict) > 0

def dict_builder(data):
    data.sort(reverse=True)
    chips_dict = defaultdict(list)
    operation_dict = defaultdict(list)
    for line in data:
        # print(line)
        ln = line.split(' ')
        if 'value' in ln:
            chips_dict[int(ln[5])].append(int(ln[1]))
        else:
            operation_dict[int(ln[1])] = [(ln[5], int(ln[6])), (ln[10], int(ln[11]))]
    # print(chips_dict)
    # print(operation_dict)
    return chips_dict, operation_dict

def resolve_bots(chips, operations):
    outputs = defaultdict(list)
    to_run = [i for i in operations.keys()]
    while len(to_run) > 0:
        skipped = []
        for bot in to_run:
            for k in range(2):
                fun = min if k == 0 else max
                if len(chips[bot]) < 2:
                    skipped.append(bot)
                    break
                if operations[bot][k][0] == 'bot':
                    chips[operations[bot][k][1]].append(fun(chips[bot]))
                else:
                    outputs[operations[bot][k][1]].append(fun(chips[bot]))
        to_run = deepcopy(skipped)
            
    return chips, outputs

     
     

data = open('2016_10.txt').read().split('\n')
res = dict_builder(data)
cps, ops = resolve_bots(res[0], res[1])
print(f"Part A: {list(cps.keys())[list(cps.values()).index([61, 17])]}")
print(f"Part B: {ops[0][0] * ops[1][0] * ops[2][0]}")