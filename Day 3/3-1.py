rankings = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

total_ranking = 0
with open('rucksacks', 'r') as rucksacks_file:
    contents = rucksacks_file.read()
    rucksacks = contents.splitlines()

for rucksack in rucksacks:
    section_one = rucksack[:len(rucksack) // 2]
    section_two = rucksack[len(rucksack) // 2:]

    for letter in section_one:
        if letter in section_two:
            double_letter = letter

    total_ranking += rankings.index(double_letter) + 1

print(total_ranking)

