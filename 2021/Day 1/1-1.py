with open("measurements", 'r') as instructions_file:
    depths = instructions_file.read().splitlines()
increases = 0
for depth_index in range(len(depths)):
    if int(depths[depth_index]) > int(depths[depth_index - 1]):
        increases += 1

print("Number of increases:", increases)



