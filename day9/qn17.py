file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
inputs = []
for x in inputvalues:
    movement, number = x.split(' ')
    inputs.append([movement, int(number)])
print(inputs)
Ti = 0
Tj = 0
Hi = 0
Hj = 0

A = set()


def moveH(movement):
    global Hi, Hj, Ti, Tj
    if movement == 'R':
        Hj += 1
    if movement == 'L':
        Hj -= 1
    if movement == 'U':
        Hi -= 1
    if movement == 'D':
        Hi += 1


def moveT():
    global Hi, Hj, Ti, Tj
    if (Ti == Hi) and (Tj != Hj):
        if ((Hj-Tj) >= 2):
            Tj += 1
        elif ((Hj-Tj) <= -2):

            Tj -= 1
    elif (Tj == Hj) and (Ti != Hi):
        if ((Hi-Ti) >= 2):

            Ti += 1
        elif ((Hi-Ti) <= -2):

            Ti -= 1
    elif (Ti != Hi) and (Tj != Hj):
        if ((Hi-Ti) <= -2 and (Hj-Tj) == 1):
            Ti -= 1
            Tj += 1
        elif ((Hi-Ti) <= -2 and (Hj-Tj) == -1):
            Ti -= 1
            Tj -= 1
        elif ((Hi-Ti) == -1 and (Hj-Tj) >= 2):
            Ti -= 1
            Tj += 1
        elif ((Hi-Ti) <= -2 and (Hj-Tj) >= 1):
            Ti -= 1
            Tj -= 1
        elif ((Hi-Ti) >= 2 and (Hj-Tj) == 1):
            Ti += 1
            Tj += 1
        elif ((Hi-Ti) >= 2 and (Hj-Tj) == -1):
            Ti += 1
            Tj -= 1
        elif ((Hi-Ti) == 1 and (Hj-Tj) <= -2):
            Ti += 1
            Tj -= 1
        elif ((Hi-Ti) == 1 and (Hj-Tj) >= 2):
            Ti += 1
            Tj += 1
        elif ((Hi-Ti) == -1 and (Hj-Tj) <= -2):
            Ti -= 1
            Tj -= 1


for x in inputs:
    print(x[0], x[1])
    for i in range(x[1]):
        moveH(x[0])

        moveT()
        # print(Hi, Hj, Ti, Tj)
        A.add(str(Ti)+','+str(Tj))

print(Ti, Tj)
print(len(A))
