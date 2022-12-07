priorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
total_priority = 0

with open('rucksacks', 'r') as rucksacks_file:
    rucksacks = rucksacks_file.read().splitlines()

for rucksack in rucksacks:
    compartment_one = rucksack[:len(rucksack) // 2]
    compartment_two = rucksack[len(rucksack) // 2:]
    for item in compartment_one:
        if item in compartment_two:
            total_priority += priorities.index(item) + 1
            break

print(total_priority)


