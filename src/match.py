import inning as inn

def print_inning_details(current_inning):
	print(current_inning.runs_so_far)
	print(current_inning.fow)
	print(current_inning.overs)

	for batsman in current_inning.batsman_list:
		print(batsman + ':' + str(sum(current_inning.batsman_scores[batsman])))


def get_batsman_list():
	batsman_list = []

	for i in range(1, 12):
		batsman_list.append('No-'+str(i))

	return batsman_list

for _ in range(100):
	batsmen_list = get_batsman_list()
	first_inn = inn.Inning(batsmen_list)
	first_inn.start()

	second_inn = inn.Inning(batsmen_list, first_inn.runs_so_far+1)
	second_inn.start()
	
	#print_inning_details(first_inn)
	#print_inning_details(second_inn)

	print("Result")

	if second_inn.runs_so_far > first_inn.runs_so_far:
		print("Team B win by "+ str(10-second_inn.wkts_so_far) + " wickets")
	elif second_inn.runs_so_far == first_inn.runs_so_far:
		print("Match tied.")
	else:
		print("Team A win by " + str(first_inn.runs_so_far - second_inn.runs_so_far) + " runs")

	
