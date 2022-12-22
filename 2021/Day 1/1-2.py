with open("measurements", 'r') as instructions_file:
    depths = instructions_file.read().splitlines()
increases = 0
triplets = []
for depth_index in range(2, len(depths)):
    triplets.append(int(depths[depth_index]) + int(depths[depth_index - 1]) + int(depths[depth_index - 2]))

for triplet_index in range(len(triplets)):
    if int(triplets[triplet_index]) > int(triplets[triplet_index - 1]):
        increases += 1

print("Number of increases:", increases)
