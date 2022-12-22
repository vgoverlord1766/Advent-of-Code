with open('rounds', 'r') as rounds_file:
    rounds = rounds_file.read().splitlines()
total_score = 0

for individual_round in rounds:
    opponent_choice = individual_round.split(' ')[0]
    end_result = individual_round.split(' ')[1]

    if end_result == "X":
        if opponent_choice == "A":
            total_score += 3
        if opponent_choice == "B":
            total_score += 1
        if opponent_choice == "C":
            total_score += 2

    if end_result == "Y":
        if opponent_choice == "A":
            total_score += 1
        if opponent_choice == "B":
            total_score += 2
        if opponent_choice == "C":
            total_score += 3
        total_score += 3

    if end_result == "Z":
        if opponent_choice == "A":
            total_score += 2
        if opponent_choice == "B":
            total_score += 3
        if opponent_choice == "C":
            total_score +=1
        total_score +=6

print(total_score)


