import inning as inn
import time
import threading
import json

def print_inning_details(current_inning):
	inning_details = dict()
	inning_details["score"] = str(current_inning.runs_so_far)
	inning_details["wickets"] = str(current_inning.wkts_so_far)
	inning_details["overs"] = str(current_inning.overs)
	
	inning_details["striker"] = current_inning.striker +":" + \
								str(current_inning.batsman_scores[current_inning.striker])
	
	inning_details["nonstriker"] = current_inning.non_striker +":" + \
								   str(current_inning.batsman_scores[current_inning.non_striker])
	
	inning_details["allscores"] = str(current_inning.batsman_scores)
	
	json_object = json.dumps(inning_details, indent = 4)
	print(json_object)

def get_batsman_list():
	team_a, team_b = [], []
	f = open("src/players.txt", "r")

	for i in range(22):
		line = f.readline()
		line = line.split(",")
		player_id, name = line[0].strip(), line[1].strip()

		if i < 11:
			team_a.append(name)
		else:
			team_b.append(name)

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
	time_span += 2
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

	
