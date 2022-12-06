with open('assignments', 'r') as assignments_file:
    assignments = assignments_file.read().splitlines()
assignment_count = 0

for assignment_pair in assignments:
    first_assignment = assignment_pair.split(",")[0]
    second_assignment = assignment_pair.split(",")[1]

    first_assignment_start = int(first_assignment.split("-")[0])
    first_assignment_end = int(first_assignment.split("-")[1])

    second_assignment_start = int(second_assignment.split("-")[0])
    second_assignment_end = int(second_assignment.split("-")[1])

    if second_assignment_start <= first_assignment_start <= second_assignment_end:
        assignment_count += 1
    elif second_assignment_start <= first_assignment_end <= second_assignment_end:
        assignment_count += 1
    elif first_assignment_start <= second_assignment_start <= first_assignment_end:
        assignment_count += 1
    elif first_assignment_start <= second_assignment_end <= first_assignment_end:
        assignment_count += 1

print(assignment_count)
