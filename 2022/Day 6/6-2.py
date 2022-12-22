with open('datastream', 'r') as datastream_file:
    datastream = datastream_file.read()

for letter_number in range(len(datastream)):
    letter_set = []
    for x in range(14):
        letter_set.append(datastream[letter_number + x])

    no_duplicates_letter_set = [*set(letter_set)]
    if len(no_duplicates_letter_set) == 14:
        break

print(letter_number + 14)