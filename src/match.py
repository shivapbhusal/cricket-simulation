import inning as inn
import time

def print_inning_details(current_inning):
	print(current_inning.runs_so_far)
	print(current_inning.fow)
	print(current_inning.overs)

	for batsman in current_inning.batsman_list:
		print(batsman + ':' + str(sum(current_inning.batsman_scores[batsman])) + ':'+str(len(current_inning.batsman_scores[batsman])))


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
first_inn.start()

while time_span <= 30:
	print_inning_details(first_inn)
	time_span += 30
	time.sleep(2)

second_inn = inn.Inning(team_b, first_inn.runs_so_far+1)
second_inn.start()
	
while time_span <= 60:
	print_inning_details(second_inn)
	time_span += 30
	time.sleep(2)

print("Result")

if second_inn.runs_so_far > first_inn.runs_so_far:
	print("Team B win by "+ str(10-second_inn.wkts_so_far) + " wickets")
elif second_inn.runs_so_far == first_inn.runs_so_far:
	print("Match tied.")
else:
	print("Team A win by " + str(first_inn.runs_so_far - second_inn.runs_so_far) + " runs")

	
