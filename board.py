import re

class Board:
	COMM = "Community Chest"
	CHANCE = "Chance"
	GO_TO_JAIL = "Go to Jail"
	JAIL = "Jail"

	def __init__(self):
		self.props = []
		self.prop_to_pos = {}
		self.pos_to_prop = {}
		self.create_board_maps()

	def create_board_maps(self):
		with open('txt/board.txt') as f:
			for line in f:
				pos, prop_name, color = line.strip().split(",")
				pos = int(pos)-1
				self.props.append(prop_name)
				if prop_name in self.prop_to_pos:
					self.prop_to_pos[prop_name].append(pos)
				else:
					self.prop_to_pos[prop_name] = [pos]
				self.pos_to_prop[pos] = prop_name