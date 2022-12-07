crates = [["H", "R", "B", "D", "Z", "F", "L", "S"], ["R", "M", "B", "Z", "R"], ["Z", "L", "C", "H", "N", "S"],
           ["S", "C", "F", "J"], ["P", "G", "H", "W", "R", "Z", "B"], ["V", "J", "Z", "G"," D", "N", "M", "T"],
            ["G", "L", "N", "W", "F", "S", "P", "Q"], ["M", "Z", "R"], ["M", "C", "L", "G", "V", "R", "T"]]

with open('instructions', 'r') as instructions_file:
    instructions = instructions_file.read().splitlines()[10:]

for instruction in instructions:
    starting_column_number = int(instruction.split(" ")[3])
    ending_column_number = int(instruction.split(" ")[5])
    number_of_boxes_to_move = int(instruction.split(" ")[1])

    starting_column = crates[starting_column_number - 1]
    ending_column = crates[ending_column_number - 1]

    print("Number to move:" + str(number_of_boxes_to_move))
    boxes_to_move = starting_column[len(starting_column) - number_of_boxes_to_move:]
    print(boxes_to_move)
    print(starting_column)
    ending_column.extend(boxes_to_move)
    n = len(ending_column)
    k = len(ending_column) - number_of_boxes_to_move
    for i in range(0, n - k):
        starting_column.pop()
    print(starting_column)


print(instructions)

for stack in crates:
    print(stack[-1])
