with open('monkeys', 'r') as instructions_file:
    unformatted_monkeys = instructions_file.read().splitlines()

monkeys = []
for unformatted_monkey in unformatted_monkeys:
    monkey = {}
    split_monkey = unformatted_monkey.split(": ")
    monkey["name"] = split_monkey[0]
    if split_monkey[1].isdigit():
        monkey["is_integer"] = True
        monkey["integer"] = int(split_monkey[1])
    else:
        monkey["is_integer"] = False
        monkey["first_monkey"] = split_monkey[1].split(" ")[0]
        monkey["operation"] = split_monkey[1].split(" ")[1]
        monkey["second_monkey"] = split_monkey[1].split(" ")[2]

    monkeys.append(monkey)

print(monkeys)

monkeys_that_have_called = []

has_root_called = False

while not has_root_called:
    for monkey in monkeys:
        if monkey["is_integer"]:
            monkeys_that_have_called.append(monkey)
            if monkey["name"] == "root":
                has_root_called == True
        else:
            calculation_answer = 0
            for finding_monkey in monkeys:
                if finding_monkey["name"] == monkey["second_monkey"]:
                    first_monkey = finding_monkey
                if finding_monkey["name"] == monkey["second_monkey"]:
                    second_monkey = finding_monkey
            if first_monkey["is_integer"] and second_monkey["is_integer"]:
                first_monkey_integer = first_monkey["integer"]
                second_monkey_integer = second_monkey["integer"]
                if monkey["operation"] == "+":
                    calculation_answer = first_monkey_integer + second_monkey_integer
                elif monkey["operation"] == "-":
                    calculation_answer = first_monkey_integer - second_monkey_integer
                elif monkey["operation"] == "*":
                    calculation_answer = first_monkey_integer * second_monkey_integer
                elif monkey["operation"] == "/":
                    calculation_answer = first_monkey_integer / second_monkey_integer

                monkey["is_integer"] = True
                monkey["integer"] = calculation_answer



print(monkeys_that_have_called)
