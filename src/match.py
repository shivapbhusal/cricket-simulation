import inning as inn

first_inn = inn.Inning()
first_inn.start()

print(first_inn.event_list)
print(first_inn.runs_so_far)
print(first_inn.wkts_so_far)
print(first_inn.balls_so_far)
print(first_inn.fow)

second_inn = inn.Inning(first_inn.runs_so_far)
second_inn.start()

print(second_inn.event_list)
print(second_inn.runs_so_far)
print(second_inn.wkts_so_far)
print(second_inn.balls_so_far)
print(second_inn.fow)

