file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
map = []
maxweight = 1
for i in range(len(inputvalues)):
    map.append([])
    for j in inputvalues[i]:
        map[i].append(int(j))
for i in map:
    print(i)
rows = len(map)
columns = len(map)

count = 0
for i in range(1, rows-1):
    for j in range(1, columns-1):
        lefttree = 0
        righttree = 0
        downtree = 0
        uptree = 0
        xsxcsd = []
        for k in range(i-1, -1, -1):

            uptree += 1
            if map[k][j] >= map[i][j]:
                break
        for l in range(i+1, rows):

            downtree += 1
            if map[l][j] >= map[i][j]:
                break
        for m in range(j-1, -1, -1):

            lefttree += 1
            if map[i][m] >= map[i][j]:
                break
        for n in range(j+1, columns):
            xsxcsd.append(map[i][n])
            righttree += 1
            if map[i][n] >= map[i][j]:
                break
        weight = lefttree * righttree * uptree * downtree
        if weight > maxweight:
            maxweight = weight
print(maxweight)
