file = open("input.txt", "r")
values = file.read()
calories = values.splitlines()

totalcalories = []
total = 0
for calorie in calories:
    if calorie != "":
        total = total + int(calorie)
    else:
        totalcalories.append(total)
        total = 0

totalcalories.sort(reverse=True)

print("highest calorie: ", totalcalories[0])
print("Sum of 3 highest calories: ",
      totalcalories[0]+totalcalories[1] + totalcalories[2])
