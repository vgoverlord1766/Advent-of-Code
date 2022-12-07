crates = ["H", "R", "B", "D", "Z", "F", "L", "S"], ["R", "M", "B", "Z", "R"], ["Z", "L", "C", "H", "N", "S"], \
         ["S", "C", "F", "J"], ["P", "G", "H", "W", "R", "Z", "B"], ["V", "J", "Z", "G", " D", "N", "M", "T"], \
         ["G", "L", "N", "W", "F", "S", "P", "Q"], ["M", "Z", "R"], ["M", "C", "L", "G", "V", "R", "T"]

with open('instructions', 'r') as instructions_file:
    instructions = instructions_file.read().splitlines()[10:]

for instruction in instructions:
    starting_column = crates[int(instruction.split(" ")[3]) - 1]
    ending_column = crates[int(instruction.split(" ")[5]) - 1]
    number_of_boxes_to_move = int(instruction.split(" ")[1])

    boxes_to_move = starting_column[len(starting_column) - number_of_boxes_to_move:]


    for x in range(number_of_boxes_to_move):
        starting_column.pop()
    ending_column.extend(boxes_to_move)

top_crates = ""
for stack in crates:
    top_crates += stack[-1]
print(top_crates)
