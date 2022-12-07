priorities = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "crates", "T", "U", "V", "W", "X", "Y", "Z"]
total_priority = 0
with open('rucksacks', 'r') as rucksacks_file:
    rucksacks = rucksacks_file.read().splitlines()

for counter in range(0, len(rucksacks), 3):
    first_rucksack = rucksacks[counter]
    second_rucksack = rucksacks[counter + 1]
    third_rucksack = rucksacks[counter + 2]

    for item in first_rucksack:
        if item in second_rucksack and item in third_rucksack:
            total_priority += priorities.index(item) + 1
            break

    counter += 2

print(total_priority)
