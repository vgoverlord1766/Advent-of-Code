with open('encryption', 'r') as instructions_file:
    original_number_set = instructions_file.read().splitlines()

with open('encryption', 'r') as instructions_file:
    new_number_set = instructions_file.read().splitlines()

for number in range(len(original_number_set)):
    original_number_set[number] = int(original_number_set[number])
    new_number_set[number] = int(new_number_set[number])

number_of_numbers = len(original_number_set)

def re_order(number, new_number_set_edited):
    initial_index = new_number_set_edited.index(number)
    offset = number % (len(new_number_set_edited) - 1)
    new_index = initial_index + offset
    if new_index >= len(new_number_set_edited):
        new_index = new_index % len(new_number_set_edited) + 1
    elif new_index == 0:  # I think this is one of the places I kept struggling to get it right
        new_index = 0 if offset > 0 else len(new_number_set_edited)
    new_number_set_edited.pop(initial_index)
    new_number_set_edited.insert(new_index, number)
    return new_number_set_edited


for number in original_number_set:
    new_number_set = re_order(number, new_number_set)

print(new_number_set)
where_is_zero = new_number_set.index(0)
one_thousand_number = new_number_set[(1000 + where_is_zero) % len(new_number_set)]
two_thousand_number = new_number_set[(2000 + where_is_zero) % len(new_number_set)]
three_thousand_number = new_number_set[(3000 + where_is_zero) % len(new_number_set)]

print(one_thousand_number + two_thousand_number + three_thousand_number)

