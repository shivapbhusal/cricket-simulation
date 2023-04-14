import random
import utilities as utils
import collections
import time
import threading
from enum import Enum

class Status(Enum):
	NOT_YET_ON_CREASE = 0,
	ON_STRIKE = 1,
	NON_STRIKER = 2,
	OUT = 3

"""
Class to represent attributes of a player
based on their batting order.
Player Status : 0 - not at the crease yet
1 - on strike
2 - non -strker
3 - out
"""
class Player:
	def __init__(self, batting_order, name, balls = 0, runs = 0, status = Status.NOT_YET_ON_CREASE):
		self.batting_order = batting_order
		self.name = name
		self.balls = balls
		self.runs = runs
		self.status = status
	
	def score_runs(self, runs):
		self.runs += runs
	
	def face_ball(self):
		self.balls +=  1
	
	def strike_rotate(self):
		if self.status == 1:
			self.status = 2
		else:
			self.status = 1
	
	def change_status(self, new_status):
		self.status = new_status

class Inning:
	def __init__(self, batsman_list, target= float('inf')):
		self.target = target
		self.runs_so_far = 0
		self.wkts_so_far = 0
		self.balls_so_far = 0
		self.overs = 0
		self.event_list = []
		self.fow = []
		self.batsman_list = batsman_list
		self.batsman_scores = collections.defaultdict(int)
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
			self.striker.status = Status.ON_STRIKE
			self.non_striker.status = Status.NON_STRIKER

		if ball_event == -1:
			self.striker.face_ball()
			self.striker.status = Status.OUT
			self.striker = self.batsman_list[self.wkts_so_far+1]

		if self.balls_so_far % 6 == 0:
			self.striker, self.non_striker = self.non_striker, self.striker

	def start(self):
		# Needs Modification based on player.
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
				# Here, ball_event can be considered run.
				self.striker.score_runs(ball_event)
				self.striker.face_ball()

			time.sleep(1)







