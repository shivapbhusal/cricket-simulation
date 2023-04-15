from flask import Flask, jsonify, request, render_template
import inning as inn
import time
import threading
import json
from multiprocessing import Process

app = Flask(__name__)

# Global variables to keep inning info
first_inning = None
second_inning = None

def prestart_inning():
	global first_inning
	global second_inning

	team_a, team_b, bowlers_for_a, bowlers_for_b = get_player_list()
	first_inning = inn.Inning(team_a, bowlers_for_a)

	first_inning.start()
	time.sleep(30)

	second_inning = inn.Inning(team_b, bowlers_for_b, first_inning.runs_so_far + 1)
	second_inning.start()


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/match')
def get_match_details():
	global first_inning
	global second_inning
	match_details = {0: get_inning_info(first_inning),
		  1: get_inning_info(second_inning)}
	
	return jsonify(match_details)

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

def get_inning_info(current_inning):
	if current_inning == None:
		return {}
	
	inning_details = dict()
	inning_details["target"] = current_inning.target
	inning_details["score"] = str(current_inning.runs_so_far)
	inning_details["wickets"] = str(current_inning.wkts_so_far)
	inning_details["overs"] = str(current_inning.overs)

	inning_details["allbatters"] = \
		get_dictionary_list_from_batter_list(current_inning.batsman_list)
	
	inning_details["allbowlers"] = \
		get_dictionary_list_from_bowler_list(current_inning.bowler_list)

	return inning_details

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

#Tell the app to run
#First argument will be a port
if __name__ == "__main__":
	#Create and start a process for init()
	t = threading.Thread(target=prestart_inning)
	t.daemon = True
	t.start()
	app.run(port = 4000)