with open("day08.txt", 'r') as file:
    tree_map = [line.strip() for line in file.readlines()]

#print(tree_map)
            
#pt 1
visible_trees = 0

for i, row in enumerate(tree_map):
    #print(i, row)
    #add all trees from first and last row and just go on..
    if i in [0, len(tree_map)-1]:
        visible_trees += len(row)
        continue
    for j, tree in enumerate(list(row)):
        if j in [0, len(row)-1]:
            #print(f"adding {tree} on index {j} to visible trees")
            visible_trees += 1
            continue
        tree_heigth = int(tree)
        trees_left = [int(row[x]) for x in range(0,j)]
        trees_right = [int(row[x]) for x in range(j+1, len(row))]
        trees_above = [int(x[j]) for x in tree_map[:i]]
        trees_below = [int(x[j]) for x in tree_map[i+1:]]

        if all(x < tree_heigth for x in trees_left):
            #print(f"tree {tree_heigth} on row {i} index {j} is visible from the left")
            #print(f"trees_left: {trees_left}")
            visible_trees += 1
            continue

        if all(x < tree_heigth for x in trees_right):
            #print(f"tree {tree_heigth} on row {i} index {j} is visible from the right")
            #print(f"trees_right: {trees_right}")
            visible_trees += 1
            continue

        if all(x < tree_heigth for x in trees_above):
            #print(f"tree {tree_heigth} on row {i} index {j} is visible from above")
            #print(f"trees_above: {trees_above}")
            visible_trees += 1
            continue

        if all(x < tree_heigth for x in trees_below):
            #print(f"tree {tree_heigth} on row {i} index {j} is visible from below")
            #print(f"trees_below: {trees_below}")
            visible_trees += 1
            continue

print("visible trees: ", visible_trees)

#pt 2
scenic_scores = []

for i, row in enumerate(tree_map):
    visible = False
    #skip edge trees
    if i in [0, len(tree_map)-1]:
        continue
    for j, tree in enumerate(list(row)):
        if j in [0, len(row)-1]:
            #skip edge trees
            continue
        tree_heigth = int(tree)
        trees_left = [int(row[x]) for x in range(0,j)]
        trees_right = [int(row[x]) for x in range(j+1, len(row))]
        trees_above = [int(x[j]) for x in tree_map[:i]]
        trees_below = [int(x[j]) for x in tree_map[i+1:]]

        if all(x < tree_heigth for x in trees_left) and not visible:
            visible = True

        if all(x < tree_heigth for x in trees_right) and not visible:
            visible = True

        if all(x < tree_heigth for x in trees_above) and not visible:
            visible = True

        if all(x < tree_heigth for x in trees_below) and not visible:
            visible = True

        if visible:
            #visible tree is a starting point here, reverse order of trees on left and above
            trees_left.reverse()
            trees_above.reverse()


            left_visibility_list = []
            right_visibility_list = []
            top_visibility_list = []
            bottom_visibility_list = []

            for x in trees_left:
                left_visibility_list.append(x)
                if x >= tree_heigth:
                    break

            for x in trees_right:
                right_visibility_list.append(x)
                if x >= tree_heigth:
                    break

            for x in trees_above:
                top_visibility_list.append(x)
                if x >= tree_heigth:
                    break

            for x in trees_below:
                bottom_visibility_list.append(x)
                if x >= tree_heigth:
                    break

            scenic_scores.append(len(left_visibility_list) * len(right_visibility_list) * len(top_visibility_list) * len(bottom_visibility_list))

print("highest scenic score: ", max(scenic_scores))



