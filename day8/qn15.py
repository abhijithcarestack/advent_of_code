file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
map = []
for i in range(len(inputvalues)):
    map.append([])
    for j in inputvalues[i]:
        map[i].append(int(j))
for i in map:
    print(i)
rows = len(map)
columns = len(map)
print(rows, columns)
count = 0
for i in range(1, rows-1):
    for j in range(1, columns-1):
        if (map[i][j] > max([map[k][j] for k in range(0, i)])) or (map[i][j] > max([map[k][j] for k in range(i+1, rows)])) or (map[i][j] > max([map[i][l] for l in range(0, j)])) or (map[i][j] > max([map[i][l] for l in range(j+1, columns)])):
            count += 1

print(count)
