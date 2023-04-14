import inning as inn
import time
import threading
import json

def get_dictionary_list_from_batter_list(batter_list):
	all_batters = []
	for player in batter_list:
		all_batters.append({
			"name" : player.name,
			"batting_order" : player.batting_order,
			"runs" : player.runs,
			"balls" : player.balls,
			"status" : player.status.name
		})
	
	return all_batters


def print_inning_details(current_inning):
	inning_details = dict()
	inning_details["target"] = current_inning.target
	inning_details["score"] = str(current_inning.runs_so_far)
	inning_details["wickets"] = str(current_inning.wkts_so_far)
	inning_details["overs"] = str(current_inning.overs)

	inning_details["allbatters"] = \
		get_dictionary_list_from_batter_list(current_inning.batsman_list)
	
	print(json.dumps(inning_details, indent = 4))

def get_batsman_list():
	team_a, team_b = [], []
	f = open("src/players.txt", "r")

	for i in range(22):
		line = f.readline()
		line = line.split(",")
		player_id, name = line[0].strip(), line[1].strip()
		# Check for this line if it causes any issues
		# If 0 - should be 0. If 11 should be 11, if 21 should be 10.
		batting_order = i % 11
		player = inn.Player(batting_order, name)
		
		"""
		First 11 players in team A.
		Next 11 players in team B.
		"""
		if i < 11:
			team_a.append(player)
		else:
			team_b.append(player)

	return team_a, team_b

first_inn, second_inn = None, None
time_span = 0

team_a, team_b = get_batsman_list()
first_inn = inn.Inning(team_a)

th = threading.Thread(target = first_inn.start)
th.start()
print('match started.')

while time_span <= 120:
	print_inning_details(first_inn)
	time_span += 1
	# Time sleep per ball
	time.sleep(1)

th.join()

second_inn = inn.Inning(team_b, first_inn.runs_so_far+1)
th = threading.Thread(target = second_inn.start)
th.start()

print("Second inning started")
	
while time_span <= 240:
	print('Target: '+str(second_inn.target))
	print_inning_details(second_inn)
	time_span += 2
	time.sleep(1)

th.join()

print("Result")

if second_inn.runs_so_far > first_inn.runs_so_far:
	print("Team B win by "+ str(10-second_inn.wkts_so_far) + " wickets")
elif second_inn.runs_so_far == first_inn.runs_so_far:
	print("Match tied.")
else:
	print("Team A win by " + str(first_inn.runs_so_far - second_inn.runs_so_far) + " runs")

	
