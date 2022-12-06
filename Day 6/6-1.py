with open('datastream', 'r') as datastream_file:
    datastream = datastream_file.read()

for letter_number in range(len(datastream)):
    letter_group = [datastream[letter_number], datastream[letter_number + 1], datastream[letter_number + 2],
                    datastream[letter_number + 3]]
    shortened_letter_group = [*set(letter_group)]
    if len(shortened_letter_group) == 4:
        break

print(letter_number + 4)
