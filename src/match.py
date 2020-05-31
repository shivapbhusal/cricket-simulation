import inning as inn

for _ in range(3):
	first_inn = inn.Inning()
	first_inn.start()
	print(first_inn.runs_so_far)
	print(first_inn.fow)

	second_inn = inn.Inning(first_inn.runs_so_far+1)
	second_inn.start()

	print(second_inn.runs_so_far)
	print(second_inn.fow)

