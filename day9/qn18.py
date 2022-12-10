file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
inputs = []
for x in inputvalues:
    movement, number = x.split(' ')
    inputs.append([movement, int(number)])
print(inputs)

Knots = {
    0: [0, 0],
    1: [0, 0],
    2: [0, 0],
    3: [0, 0],
    4: [0, 0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0],
    8: [0, 0],
    9: [0, 0],
}

A = set()


def moveH(movement):
    if movement == 'R':
        Knots[0][1] += 1
    if movement == 'L':
        Knots[0][1] -= 1
    if movement == 'U':
        Knots[0][0] -= 1
    if movement == 'D':
        Knots[0][0] += 1


def move(knotnumber):
    if (Knots[knotnumber][0] == Knots[knotnumber-1][0]) and (Knots[knotnumber][1] != Knots[knotnumber-1][1]):
        if ((Knots[knotnumber-1][1]-Knots[knotnumber][1]) >= 2):
            Knots[knotnumber][1] += 1
        elif ((Knots[knotnumber-1][1]-Knots[knotnumber][1]) <= -2):

            Knots[knotnumber][1] -= 1
    elif (Knots[knotnumber][1] == Knots[knotnumber-1][1]) and (Knots[knotnumber][0] != Knots[knotnumber-1][0]):
        if ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) >= 2):

            Knots[knotnumber][0] += 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) <= -2):

            Knots[knotnumber][0] -= 1
    elif (Knots[knotnumber][0] != Knots[knotnumber-1][0]) and (Knots[knotnumber][1] != Knots[knotnumber-1][1]):
        if ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) <= -2 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) == 1):
            Knots[knotnumber][0] -= 1
            Knots[knotnumber][1] += 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) <= -2 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) == -1):
            Knots[knotnumber][0] -= 1
            Knots[knotnumber][1] -= 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) == -1 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) >= 2):
            Knots[knotnumber][0] -= 1
            Knots[knotnumber][1] += 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) <= -2 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) >= 1):
            Knots[knotnumber][0] -= 1
            Knots[knotnumber][1] -= 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) >= 2 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) == 1):
            Knots[knotnumber][0] += 1
            Knots[knotnumber][1] += 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) >= 2 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) == -1):
            Knots[knotnumber][0] += 1
            Knots[knotnumber][1] -= 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) == 1 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) <= -2):
            Knots[knotnumber][0] += 1
            Knots[knotnumber][1] -= 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) == 1 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) >= 2):
            Knots[knotnumber][0] += 1
            Knots[knotnumber][1] += 1
        elif ((Knots[knotnumber-1][0]-Knots[knotnumber][0]) == -1 and (Knots[knotnumber-1][1]-Knots[knotnumber][1]) <= -2):
            Knots[knotnumber][0] -= 1
            Knots[knotnumber][1] -= 1


for x in inputs:
    # print(x[0], x[1])
    for i in range(x[1]):
        moveH(x[0])
        for i in range(1, 10):
            move(i)
            # print(Knots)
        A.add(str(Knots[9][0])+','+str(Knots[9][1]))


print(len(A))
