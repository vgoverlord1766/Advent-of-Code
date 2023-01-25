import numpy as np

with open('example_measurements', 'r') as instructions_file:
    instructions = instructions_file.read().splitlines()

instructions_array = []
for instruction in instructions:
    instruction_list = []
    for instruction_number in instruction:
        instruction_list.append(instruction_number)
    instructions_array.append(instruction_list)

instructions_transposed = np.transpose(instructions_array)
gamma_rate = []
epsilon_rate = []
for column in instructions_transposed:
    zero_count = 0
    one_count = 0
    for row in column:
        if row == "0": zero_count += 1
        if row == "1": one_count += 1

    if zero_count > one_count: gamma_rate.append("0")
    if one_count > zero_count: gamma_rate.append("1")

    if zero_count < one_count: epsilon_rate.append("0")
    if one_count < zero_count: epsilon_rate.append("1")

gamma_rate_string = ("".join(gamma_rate))
epsilon_rate_string = ("".join(epsilon_rate))
print("Gamma Rate: " + str(int(gamma_rate_string,2)))
print("Epsilon Rate: "+ str(int(epsilon_rate_string,2)))
print("Total Power Consumption: " + str(int(gamma_rate_string,2) * int(epsilon_rate_string,2)))


