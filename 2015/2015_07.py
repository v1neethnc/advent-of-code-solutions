# Advent of Code, 2015
# Day 7: Some Assembly Required
# https://adventofcode.com/2015/day/7
# https://github.com/v1neethnc/advent-of-code-solutions


class circuit_evaluator:
	
	def dict_builder(self):
		self.vals_dict = {}
		with open("2015_07.txt") as file_data:
			data = [i.strip().split(' -> ') for i in file_data]
			for ind in range(len(data)):
				if ' ' in data[ind][0]:
					data[ind][0] = data[ind][0].split(' ')
				if data[ind][-1] not in self.vals_dict.keys():
					if isinstance(data[ind][0], str):
						self.vals_dict[data[ind][-1]] = int(data[ind][-2]) if data[ind][-2].isdigit() else [data[ind][-2]]
					else:
						self.vals_dict[data[ind][-1]] = data[ind][-2]

	def evaluate(self, gate):
		# Return the integer if gate or its value in dict is int
		if isinstance(gate, int) or (isinstance(gate, str) and gate.isdigit()):
			return int(gate)
		if isinstance(self.vals_dict[gate], int):
			return self.vals_dict[gate]
		# Get corresponding gate's value
		if len(self.vals_dict[gate]) == 1:
			return self.evaluate(self.vals_dict[gate][0])
		# NOT gate
		elif len(self.vals_dict[gate]) == 2:
			self.vals_dict[gate] = ~self.evaluate(self.vals_dict[gate][1])
			return self.vals_dict[gate]
		# Gates with two operands
		gt = self.vals_dict[gate][1]
		if gt == 'OR':
			self.vals_dict[gate] = self.evaluate(self.vals_dict[gate][0]) | self.evaluate(self.vals_dict[gate][2])
		elif gt == 'AND':
			self.vals_dict[gate] = self.evaluate(self.vals_dict[gate][0]) & self.evaluate(self.vals_dict[gate][2])
		elif gt == 'LSHIFT':
			self.vals_dict[gate] = self.evaluate(self.vals_dict[gate][0]) << self.evaluate(self.vals_dict[gate][2])
		elif gt == 'RSHIFT':
			self.vals_dict[gate] = self.evaluate(self.vals_dict[gate][0]) >> self.evaluate(self.vals_dict[gate][2])
		return self.vals_dict[gate]
	
eval = circuit_evaluator()
eval.dict_builder()
part_a = eval.evaluate('a')
print(f"Part A: {part_a}")

# New dict with updated b value
eval.dict_builder()
eval.vals_dict['b'] = part_a
part_b = eval.evaluate('a')
print(f"Part B: {part_b}")