from espncricinfo.player import Player

f = open("src/players.txt", "r")

for _ in range(11):
	line = f.readline()
	print(line)
	#p = Player(player_id)
	#print(p.batting_fielding_averages)