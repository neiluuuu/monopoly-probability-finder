import random
from board import Board

class Monopoly:

	def __init__(self, turns, jail_time_turns):
		self.board = Board()
		self.turns = turns
		self.my_pos = 0
		self.jail = False
		self.jail_time_turns = jail_time_turns
		self.end_turn_spots = [0]*40

	def play_game(self):
		for i in range(self.turns):
			self.take_turn()

	def take_turn(self):
		turn_roll_history = []
		while len(turn_roll_history) < 3:
			die1, die2 = self.roll_dice()
			turn_roll_history.append((die1, die2))
			self.move_position(die1+die2)
			self.handle_current_position()
			self.validate_position()
			if not self.check_doubles(die1, die2):
				break
			if len(turn_roll_history) == 3 and self.check_doubles(die1, die2):
				self.handle_go_to_jail()
			if self.jail:
				break
		self.end_turn_spots[self.my_pos] += 1
		self.reset_turn()

	def roll_dice(self):
		die1 = random.randint(1,6)
		die2 = random.randint(1,6)
		return die1, die2

	def change_pos(self, new_pos):
		self.my_pos = new_pos

	def move_position(self, roll):
		new_pos = (self.my_pos + roll) % 40
		self.change_pos(new_pos)

	def handle_current_position(self):
		if self.my_pos in self.board.prop_to_pos[Board.COMM]:
			self.handle_comm_chest()
		elif self.my_pos in self.board.prop_to_pos[Board.CHANCE]:
			self.handle_chance()
		elif self.my_pos in self.board.prop_to_pos[Board.GO_TO_JAIL]:
			self.handle_go_to_jail()

	def handle_comm_chest(self):
		card = random.randint(0,16)
		if card == 0:
			self.change_pos(0) # Advance to Go
		elif card == 1:
			self.handle_go_to_jail() # Go to Jail

	def handle_chance(self):
		card = random.randint(0,15)
		if card == 0:
			self.change_pos(0) # Advance to Go
		elif card == 1:
			self.change_pos(24) # Advance to Illinois Ave
		elif card == 2:
			self.change_pos(11) # Advance to St. Charles Place
		elif card == 3:
			self.go_nearest_utility() # Advance to nearest utility
		elif card == 4:
			self.go_nearest_railroad() # Go to nearest railroad
		elif card == 5:
			self.handle_go_to_jail() # Go to Jail
		elif card == 6:
			self.move_position(-3) # Go back 3 spaces
			self.handle_current_position()
		elif card == 7:
			self.change_pos(39) # Advance to Boardwalk
		elif card == 8:
			self.change_pos(5) # Take a ride on the Reading

	def handle_go_to_jail(self):
		self.change_pos(10)
		self.jail = True

	def go_nearest_utility(self):
		while self.my_pos != 12 and self.my_pos != 28:
			self.move_position(1)

	def go_nearest_railroad(self):
		while self.my_pos % 10 != 5:
			self.move_position(1)

	def validate_position(self):
		self.valid_pos()
		self.check_jail()

	def valid_pos(self):
		assert 0 <= self.my_pos <= 39

	def check_jail(self):
		if self.jail:
			assert self.my_pos == 10

	def check_doubles(self, die1, die2):
		return die1 == die2

	def reset_turn(self):
		self.jail = False

