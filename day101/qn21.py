file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
inputs = []
crt = []
cycle = 0
valuexx = 1
total = 0
for sx in inputvalues:
    if (sx == 'noop'):
        inputs.append([sx])
    else:
        task, value = sx.split(" ")
        inputs.append([task, int(value)])


for j in inputs:
    if (len(j) == 1):
        cycle += 1
        if cycle in [valuexx-1, valuexx, valuexx+1]:
            crt.append("#")
        else:
            crt.append('.')

    else:
        for i in range(2):
            cycle += 1
            if cycle % 39 in [valuexx-1, valuexx, valuexx+1]:
                crt.append("#")
            else:
                crt.append('.')
        valuexx = valuexx+j[1]

    # print(cycle, valuexx)

for i in range(len(crt)):
    if i in [xxxx*39 for xxxx in range(1, 7)]:
        print("\n")
    else:
        print(crt[i], end="")
