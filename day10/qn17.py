file = open("inputs.txt", "r")
values = file.read()
inputvalues = values.splitlines()
inputs = []
cycle = 0
valuex = 1
total = 0
for sx in inputvalues:
    if (sx == 'noop'):
        inputs.append([sx])
    else:
        task, value = sx.split(" ")
        inputs.append([task, int(value)])
print(inputs)
print(value)

# for j in inputs:
#     # print(j)
#     if (len(j) == 1):
#         cycle += 1
#         if cycle in [20+i*40 for i in range(5)]:
#             total += (cycle*value)
#             # print(cycle, value, cycle*value)

#     else:
#         for i in range(2):
#             cycle += 1
#             if cycle in [20+i*40 for i in range(5)]:
#                 total += (cycle*value)
#                 # print(cycle, value, cycle*value)
#         value = value+j[1]
#     print(cycle, value)
