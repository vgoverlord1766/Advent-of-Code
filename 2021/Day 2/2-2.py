with open('measurements', 'r') as instructions_file:
    instructions = instructions_file.read().splitlines()
depth = 0
horizontal = 0
aim = 0
for instruction in instructions:
    if instruction[0] == "f":
        horizontal += int(instruction.split(" ")[1])
        depth += int(instruction.split(" ")[1]) * aim
    if instruction[0] == "u":
        aim -= int(instruction.split(" ")[1])
    if instruction[0] == "d":
        aim += int(instruction.split(" ")[1])
print("Horizontal position x Final Depth: " + str(depth * horizontal))
