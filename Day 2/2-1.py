with open('rounds', 'r') as rounds_file:
    contents = rounds_file.read()
    rounds = contents.splitlines()

total_score = 0

for individual_round in rounds:
    opponent_choice = individual_round.split(' ')[0]
    your_choice = individual_round.split(' ')[1]

    if your_choice == "X":
        total_score += 1
        new_your_choice = "A"
    if your_choice == "Y":
        total_score += 2
        new_your_choice = "B"
    if your_choice == "Z":
        total_score +=3
        new_your_choice = "C"

    if new_your_choice == "C" and opponent_choice == "A":
        total_score += 0
    elif opponent_choice == "C" and new_your_choice == "A":
        total_score += 6
    elif new_your_choice > opponent_choice:
        total_score += 6
    elif new_your_choice == opponent_choice:
        total_score += 3

print(total_score)