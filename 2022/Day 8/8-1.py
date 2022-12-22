with open('trees', 'r') as trees_file:
    trees = trees_file.read().splitlines()
visible_trees = 0
trees_matrix = []
for tree_row in trees:
    print(tree_row)
    tree_row_matrix = []
    for x in range(len(tree_row)):
        tree_row_matrix.append(tree_row[x])
    trees_matrix.append(tree_row_matrix)

print(trees_matrix)

for tree_row in trees_matrix:
    tree_row.sort()
    for tree in tree_row:
        tree_number = tree_row.index(tree)
        for new_row in trees_matrix:
            if tree > new_row[tree_number]:
                print(tree)
                visible_trees += 1
                break
        if tree > tree_row[0]:
            print(tree)
            visible_trees += 1


print(visible_trees)

