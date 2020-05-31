import random
import utilities as utils
import collections

class Inning:
	def __init__(self, batsman_list, target= float("inf")):
		self.target = target
		self.runs_so_far = 0
		self.wkts_so_far = 0
		self.balls_so_far = 0
		self.overs = 0
		self.event_list = []
		self.fow = []
		self.batsman_list = batsman_list
		self.batsman_scores = collections.defaultdict(list)
		self.striker = batsman_list[0]
		self.non_striker = batsman_list[1]

	def change_strike(self, ball_event):
		"""
		If run is 1 or 3, change strike. 
		If event is out -- replace current batsman with the new batsman. 
		If over is completed, change the strike. 
		"""
		if ball_event == 1 or ball_event == 3:
			self.striker, self.non_striker = self.non_striker, self.striker

		if ball_event == -1:
			self.striker = self.batsman_list[self.wkts_so_far+1]

		if self.balls_so_far % 6 == 0:
			self.striker, self.non_striker = self.non_striker, self.striker

	def start(self):
		while self.runs_so_far < self.target and self.wkts_so_far < 10 and self.balls_so_far < 120:
			ball_event = utils.ball_event()
			self.balls_so_far += 1

			if ball_event == -1:
				self.wkts_so_far += 1
			else:
				self.runs_so_far += ball_event

			overs = str(self.balls_so_far // 6) + '.' + str(self.balls_so_far % 6)
			self.overs = overs
			
			if ball_event == -1:
				self.fow.append((overs, self.runs_so_far, self.wkts_so_far))

			self.event_list.append((overs, self.runs_so_far, self.wkts_so_far))

			if self.wkts_so_far < 10 and self.balls_so_far < 120:
				self.change_strike(ball_event)
			
			if ball_event > -1:
				self.batsman_scores[self.striker].append(ball_event)







