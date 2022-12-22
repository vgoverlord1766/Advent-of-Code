import math
with open('monkeys', 'r') as instructions_file:
    monkeys_string = instructions_file.read().splitlines()

monkeys = []

for x in range(0, len(monkeys_string), 7):
    monkey = {}

    starting_items = monkeys_string[x+1].replace(",", "").split(" ")[2:]
    starting_items_array = []
    for item in starting_items:
        starting_items_array.append(int(item))

    monkey["monkey_number"] = int(monkeys_string[x][7:-1])
    monkey["items"] = starting_items_array
    monkey["operation"] = monkeys_string[x+2][17:]
    monkey["test"] = int(monkeys_string[x+3].split(" ")[3])
    monkey["true"] = int(monkeys_string[x+4][25])
    monkey["false"] = int(monkeys_string[x+5][26])
    monkeys.append(monkey)

inspection_counts = [0, 0, 0, 0, 0, 0, 0, 0]
for x in range(20):
    for monkey in monkeys:
        print(monkey["items"])
        for item in monkey["items"]:
            print(item)
            if monkey["monkey_number"] == 0:
                item = math.floor(item * 7)

            if monkey["monkey_number"] == 1:
                item = math.floor(item + 5)

            if monkey["monkey_number"] == 2:
                item = math.floor(item * item)

            if monkey["monkey_number"] == 3:
                item = math.floor(item + 6)

            if monkey["monkey_number"] == 4:
                item = math.floor(item * 11)

            if monkey["monkey_number"] == 5:
                item = math.floor(item + 8)

            if monkey["monkey_number"] == 6:
                item = math.floor(item + 1)

            if monkey["monkey_number"] == 7:
                item = math.floor(item + 4)

            inspection_counts[monkey["monkey_number"]] += 1
            item = math.floor(item / 3)
            if item % monkey["test"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
                print("true")
            else:
                monkeys[monkey["false"]]["items"].append(item)
                print("false")


        monkey["items"].clear()
        print("Monkey 0:", monkeys[0]["items"])

print(inspection_counts)
