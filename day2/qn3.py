file = open("inputs.txt", "r")
values = file.read()
rounds = values.splitlines()

roundsarray = []
totalcalories = []
total = 0

for moves in rounds:
    opponent, mymove = moves.split(' ')
    roundsarray.append([opponent, mymove])

print(roundsarray)

points = 0
for round in roundsarray:
    if round[1] == 'X':
        points = points + 1
    elif round[1] == 'Y':
        points = points + 2
    elif round[1] == 'Z':
        points = points + 3

    if round[0] == 'A' and round[1] == 'X':
        points = points+3
    elif round[0] == 'B' and round[1] == 'Y':
        points = points+3
    elif round[0] == 'C' and round[1] == 'Z':
        points = points+3
    elif round[0] == 'A' and round[1] == 'Y':
        points = points+6
    elif round[0] == 'A' and round[1] == 'Z':
        points = points+0
    elif round[0] == 'B' and round[1] == 'X':
        points = points+0
    elif round[0] == 'B' and round[1] == 'Z':
        points = points+6
    elif round[0] == 'C' and round[1] == 'X':
        points = points+6
    elif round[0] == 'C' and round[1] == 'Y':
        points = points+0

print(points)
