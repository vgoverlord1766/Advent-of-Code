with open('example_measurements', 'r') as instructions_file:
    instructions = instructions_file.read().splitlines()
    instructions_file.close()

with open('example_measurements', 'r') as instructions_file:
    instructions1 = instructions_file.read().splitlines()
    instructions_file.close()

for x in range(0, len(instructions[0])):
    one_count = 0
    zero_count = 0
    more = "1"
    for instruction in instructions:
        if instruction[x] == "0": zero_count += 1
        if instruction[x] == "1": one_count += 1

    if zero_count > one_count: more = "0"
    else: more = "1"
    bad_instructions = []
    for instruction in instructions:
        if instruction[x] != more: bad_instructions.append(instruction)
    for bad_instruction in bad_instructions:
        instructions.remove(bad_instruction)

    if len(instructions) == 1: break
print("Oxygen Generator Rating: " + str(int(instructions[0],2)))

for x in range(0, len(instructions1[0])):
    one_count = 0
    zero_count = 0
    more = "0"
    for instruction in instructions1:
        if instruction[x] == "0": zero_count += 1
        if instruction[x] == "1": one_count += 1

    if one_count < zero_count: more = "1"
    else: more = "0"
    bad_instructions = []
    for instruction in instructions1:
        if instruction[x] != more: bad_instructions.append(instruction)
    for bad_instruction in bad_instructions:
        instructions1.remove(bad_instruction)
    if len(instructions1) == 1: break
print("CO2 Scrubber Rating: " + str(int(instructions1[0],2)))
print("Life Support Rating: " + str(int(instructions[0],2) * int(instructions1[0],2)))






