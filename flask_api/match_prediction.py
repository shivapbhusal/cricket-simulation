import inning as inn
import time

def get_dictionary_list_from_bowler_list(bowler_list):
	all_bowlers = []
	for player in bowler_list:
		all_bowlers.append({
			"name" : player.name,
			"bowling_order" : player.bowling_order,
			"runs" : player.runs,
			"balls" : player.balls,
			"status" : player.status.name
		})
	
	return all_bowlers


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

def get_player_list():
	team_a, team_b, bowlers_for_a, bowlers_for_b = [], [], [], []
	f = open("flask_api/players.txt", "r")

	for i in range(22):
		line = f.readline()
		line = line.split(",")
		player_id, name = line[0].strip(), line[1].strip()
		# Check for this line if it causes any issues
		# If 0 - should be 0. If 11 should be 11, if 21 should be 10.
		batting_order = i % 11
		player = inn.Player(batting_order, name, player_id)
		
		"""
		First 11 players in team A.
		Next 11 players in team B.
		"""
		if i < 11:
			team_a.append(player)
		else:
			team_b.append(player)

	# Populate bowlers for team A
	for bowling_order, player in enumerate(team_b[6:]):
		bowlers_for_a.append(inn.Bowler(bowling_order, player.name))

	# Populate bowlers for team B 
	for bowling_order, player in enumerate(team_a[6:]):
		bowlers_for_b.append(inn.Bowler(bowling_order, player.name))

	return team_a, team_b, bowlers_for_a, bowlers_for_b

team_a, team_b, bowlers_for_a, bowlers_for_b = get_player_list()

first_inning = inn.Inning(team_a, bowlers_for_a)
print("First Inning Created")
first_inning.start()
print("First Inning Started")
second_inning = inn.Inning(team_b, bowlers_for_b, first_inning.runs_so_far + 1)
print("Second Inning Created")
second_inning.start()
print("Second Inning Started")

summary = {"A": 0, "B": 0, "T": 0}

if second_inning.runs_so_far > first_inning.runs_so_far:
	summary["B"] += 1
elif second_inning.runs_so_far == first_inning.runs_so_far:
	summary["T"] += 1
else:
	summary["A"] += 1

print(summary)
