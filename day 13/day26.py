import json
file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
values = []

for x in inputvalues:
    if x != '':
        res = json.loads(x)
        values.append(res)


def findInOrder(list1, list2):

    if (len(list1) > len(list2) and len(list1) != 1 and len(list2) != 1):
        return False
    else:
        try:
            for i in range(len(list1)):
                if type(list1[i]) == list and type(list2[i]) == list:
                    flag = findInOrder(list1[i], list2[i])
                    if flag == False:
                        return False
                elif type(list1[i]) == int and type(list2[i]) == int:
                    if list1[i] == list2[i]:
                        pass
                    elif list1[i] > list2[i]:
                        return False
                    else:
                        return True
                else:
                    if type(list1[i]) == int:
                        list1[i] = [list1[i]]
                    if type(list2[i]) == int:
                        list2[i] = [list2[i]]
                    flag = findInOrder(list1[i], list2[i])
                    if flag == False:
                        return False
        except:
            pass

    return True


print(values)
total = 0
for i in range(0, len(values)//2):
    ii = i*2

    if (findInOrder(values[ii], values[ii+1])):
        print(i+1, values[ii], values[ii+1])
        total += i+1
print(total)
