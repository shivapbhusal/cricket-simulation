import random
import utilities as utils
class Inning:
	def __init__(self, target= float("inf")):
		self.target = target
		self.runs_so_far = 0
		self.wkts_so_far = 0
		self.balls_so_far = 0
		self.event_list = []
		self.fow = []

	def start(self):
		while self.runs_so_far < self.target and self.wkts_so_far < 10 and self.balls_so_far < 120:
			ball_event = utils.ball_event()
			self.balls_so_far += 1

			if ball_event == -1:
				self.wkts_so_far += 1
				self.fow.append((self.runs_so_far, self.wkts_so_far))
			else:
				self.runs_so_far += ball_event

			self.event_list.append(ball_event)







