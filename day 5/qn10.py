file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
inputs = []
for x in inputvalues:
    first, second = x.split(' from ')
    waste1, count = first.split(' ')
    stackfrom, stackto = second.split(' to ')
    inputs.append([int(count), int(stackfrom), int(stackto)])


stacks = {1: ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'],
          2: ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
          3: ['Z', 'H', 'V'],
          4: ['M', 'Z', 'J', 'F', 'G', 'H'],
          5: ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
          6: ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
          7: ['T', 'F', 'P', 'L', 'Z'],
          8: ['Q', 'V', 'W', 'S'],
          9: ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']}

for x in inputs:
    count, stackfrom, stackto = x

    pop = stacks[stackfrom][-count:]
    stacks[stackfrom] = stacks[stackfrom][:-count]
    # print(pop)
    for x in range(count):
        print(pop[x])
        stacks[stackto].append(pop[x])
    print(stacks[stackto])


# print(stacks)
string = ""
for x in range(9):
    pop = stacks[x+1].pop()
    string = string + pop
print(string)
