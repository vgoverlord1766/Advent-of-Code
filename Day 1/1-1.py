elves = []
totalCalorieCount = 0

with open('calories', 'r') as calories_file:
    contents = calories_file.read()
    calories = contents.splitlines()

for calorie_individual in calories:
    if calorie_individual != '':
        totalCalorieCount += int(calorie_individual)
    else:
        elves.append(int(totalCalorieCount))
        totalCalorieCount = 0

elves.sort()
print("Total Calories:")
print(elves[-1])
