"""
Consists of the Utilities Methods
"""
import random
import requests
from bs4 import BeautifulSoup
import json

def get_event_when_batter_stat_available(t20_stat):
	balls_faced = t20_stat[7]
	innnings = t20_stat[2]
	not_outs = t20_stat[3]
	fours = t20_stat[11]
	sixes = t20_stat[12]
	outs_percentage = (innnings - not_outs) * 100 / balls_faced
	fours_percentage = fours * 100 / balls_faced
	sixes_percentage = sixes * 100 / balls_faced
	score_distribution = []
	for i in range(outs_percentage):
		score_distribution.append(-1)
	
	for i in range(fours_percentage):
		score_distribution.append(4)
	
	for i in range(sixes_percentage):
		score_distribution.append(6)
	
	for i in range(len(score_distribution), 100):
		rest_of_scores = [1, 0, 2, 3, 1, 0]
		index = random.randint(0, len(rest_of_scores)-1)
		score_distribution.append(rest_of_scores[index])
	
	return score_distribution[random.randint(0, len(score_distribution)-1)]
	

def get_event_if_batter_stat_not_available():
	scores = [-1, 0, 1, 2, 3, 4, 6, 1, 0, 0, 1, 2, 0, 1]
	index = random.randint(0, len(scores)-1)

	return scores[index]

def ball_event(batter_id = None):
	"""
	# Returns the result of the current ball event.
	# Parameters: batsman_id (int), bowler_id(int)
	# Return Type : int : score in that ball (-1 means out) 

	Assumption : Singles and dots will occur more often than boundaries and outs. 
	First try to get next event based on stats.
	If not possible, get default way of simulation.
	"""
	try:
		player_data = json.loads(get_career_statistics(batter_id))
		t20_stat = player_data[3]
		return get_event_when_batter_stat_available(t20_stat)
	except:
		return get_event_if_batter_stat_not_available()
	
def get_next_bowler(bowler_list, current_bowler):
	"""
	Find the position of the bowler and get next bowler to bowl.
	"""
	position = bowler_list.index(current_bowler)
	if position == len(bowler_list) - 1:
		return bowler_list[0]
	else:
		return bowler_list[position + 1]


def get_career_statistics(player_id):
	url = 'https://www.espncricinfo.com/player/player-name-' + str(player_id)
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')

	table = soup.find('table')

	rows = table.findAll('tr')
	data = []
	for row in rows:
		cols = row.findAll('td')
		cols = [col.text.strip() for col in cols]
		data.append(cols)
	json_data = json.dumps(data)
	return json_data


# for i in range(100):
# print(ball_event("34102"))








