file = open("inputs.txt", "r")
values = file.read()
inputs = values.splitlines()
inputvalues = []
for x in inputs:
    first, second = x.split(',')
    lowfirst, highfirst = first.split('-')
    lowsecond, highsecond = second.split('-')
    inputvalues.append([lowfirst, highfirst, lowsecond, highsecond])

count = 0
for i in inputvalues:
    flag = 0
    for x in range(int(i[0]), int(i[1])+1):
        if x in range(int(i[2]), int(i[3])+1):
            count = count+1
            flag = 1
            break
    if flag == 0:
        for x in range(int(i[2]), int(i[3])+1):
            if x in range(int(i[0]), int(i[1])+1):
                count = count+1
                break


print(count)
