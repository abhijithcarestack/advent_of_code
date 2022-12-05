file = open("inputs.txt", "r")
values = file.read()
rounds = values.splitlines()


def get_results(a, b, c):
    dups = []
    a = list(set(a))
    b = list(set(b))
    c = list(set(c))
    for x in a:
        if x in b and x in c:
            dups.append(x)
    return dups


def getPositionsmall(a):
    return (ord(a)-ord('a')+1)


def getPositioncaps(a):
    return (ord(a)-ord('A')+27)


# print(getPositioncaps('P'))


total = 0
for i in range(len(rounds)//3):
    i = i*3
    result = get_results(rounds[i], rounds[i+1], rounds[i+2])
    for x in result:
        x = str(x)
        if x.islower():
            # print(getPositionsmall(x))
            total = total+getPositionsmall(x)
        else:
            total = total+getPositioncaps(x)

print(total)
