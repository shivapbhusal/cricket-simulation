"""
Consists of the Utilities Methods
"""
import random
def ball_event(batsman_id = None, bowler_id = None):
	"""
	# Returns the result of the current ball event.
	# Parameters: batsman_id (int), bowler_id(int)
	# Return Type : int : score in that ball (-1 means out) 

	Assumption : Singles and dots will occur more often than boundaries and outs. 
	"""
	scores = [-1, 0, 1, 2, 3, 4, 6, 1, 0, 0, 1, 2, 0, 1]
	index = random.randint(0, len(scores)-1)

	return scores[index]





