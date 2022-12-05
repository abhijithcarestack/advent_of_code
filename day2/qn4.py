file = open("inputs.txt", "r")
values = file.read()
rounds = values.splitlines()

roundsarray = []
totalcalories = []
total = 0

for moves in rounds:
    opponent, mymove = moves.split(' ')
    roundsarray.append([opponent, mymove])


win = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

lose = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

draw = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

points = 0
for round in roundsarray:
    move = ''
    if round[1] == 'X':
        points = points + 0
        move = lose[round[0]]
        print(move)
    elif round[1] == 'Y':
        points = points + 3
        move = draw[round[0]]
    elif round[1] == 'Z':
        points = points + 6
        move = win[round[0]]

    if move == 'X':
        points = points+1
    elif move == 'Y':
        points = points+2
    elif move == 'Z':
        points = points+3

print(points)
