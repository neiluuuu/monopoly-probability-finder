from board import Board
from monopoly import Monopoly
import numpy as np
import csv

class Simulator:

	def __init__(self):
		self.occurrences = [0]*40
		self.d = {}

	def run_simulations(self, turns, num):
		for i in range(num):
			game = Monopoly(turns)
			game.play_game()
			self.occurrences = [x+y for x, y in zip(self.occurrences, game.end_turn_spots)]
		self.occurrences = [occ/float(turns*num) for occ in self.occurrences]
		self.validate_percentage()
		for i in range(len(self.occurrences)):
			self.d[i] = [Board().props[i], self.occurrences[i]]

	def validate_percentage(self):
		np.testing.assert_almost_equal(sum(self.occurrences), 1.0)

	def write_output(self):
		with open('monopoly.csv', 'wb') as f:
		    writer = csv.DictWriter(f, fieldnames=["Number", "Property", "Percentage (%)"])
		    writer.writeheader()
		    for k in sorted(self.d.keys()):
		       writer.writerow({"Property": self.d[k][0], "Percentage (%)": self.d[k][1], "Number": k})

if __name__ == "__main__":
	sim = Simulator()
	sim.run_simulations(1000, 1000)
	sim.write_output()