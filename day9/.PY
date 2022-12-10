
def move(knotnumber):
    global Knots[knotnumber-1][0], Knots[knotnumber-1][1], Knots[knotnumber][0], Knots[knotnumber][1]
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
