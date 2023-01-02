
file1 = open('inputs.txt', 'r')
body = file1.read()
lines = body.splitlines()
matrix = {'S': [], 'B': []}
all = set()
i = 0
for line in lines:
    for coordinates in line.split(':'):
        x1, y1, = coordinates.split(',')
        x1, y1 = int(x1), int(y1)
        if i % 2 == 0:
            matrix['S'].append((x1, y1))
            all.add((x1, y1))
        else:
            matrix['B'].append((x1, y1))
            all.add((x1, y1))
        # prev=(x,y)
        i += 1
j = 0
a = (0, 0)
b = (0, 0)
# print(len(matrix['S']))
for j in range(len(matrix['S'])):
    for i in matrix:
        if (i == 'S'):
            a = (matrix[i][j])
        else:
            b = (matrix[i][j])
    dist = (abs(a[0]-b[0])+abs(a[1]-b[1]))
    print('dist:', dist)
    for l in range(-int(1e7), int(1e7), 1):
        z = int(2e6)
        dist2 = (abs(a[0]-l)+abs(a[1]-z))
        if (dist2 <= dist):
            # print(dist2)
            all.add((l, z))
        else:
            pass
        # for z in range(b[0]-1,-10000,-1):
        #     dist2=(abs(a[0]-z)+abs(a[1]-l))
        #     if(dist2<=dist):
        #         print(dist2)
        #         all.add((z,l))
        #     else:
        #         break
for i in range(0, 4000000):
    for y in range(0, 4000000):
        if not all.__contains__((i, y)):
            print(i, y)
count = 0
for k in all:
    if k[1] == 2000000:
        # print(k[1])
        count += 1
print(count)
