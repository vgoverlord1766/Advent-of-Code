with open('calories', 'r') as calories_file:
    calories = calories_file.read().contents.splitlines()
elves = []
totalCalorieCount = 0

for calorie_individual in calories:
    if calorie_individual != '':
        totalCalorieCount += int(calorie_individual)
    else:
        elves.append(int(totalCalorieCount))
        totalCalorieCount = 0

elves.sort()
print(elves[-1])
