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
    if (int(i[0]) in range(int(i[2]), int(i[3])+1)) and (int(i[1]) in range(int(i[2]), int(i[3])+1)):
        count = count+1
    elif (int(i[2]-1) in range(int(i[0]), int(i[1])+1)) and (int(i[3])) in range(int(i[0]), int(i[1])+1):
        count = count+1
print(count)
