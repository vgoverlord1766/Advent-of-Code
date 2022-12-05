calories = []
with open('calories.txt', 'r') as myFile:  
    contents = myFile.read()
    calories = contents.splitlines()

print(calories)
totalCalorieCount = 0
largestCalorieCount = 0
for calorie_individual in calories:
    if(calorie_individual != ''):
        totalCalorieCount += int(calorie_individual)
    else:
        if largestCalorieCount < totalCalorieCount:
            largestCalorieCount = totalCalorieCount
        totalCalorieCount = 0

print(largestCalorieCount)
