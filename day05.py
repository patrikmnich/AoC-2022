from copy import deepcopy

with open("day05.txt", 'r') as file:
    content = [item.replace('\n', '') for item  in file.readlines()]

#pt 1

columns = 9
#boxes lines
cargo_lines = content[:8]

#move instructions lines
move_instructions = content[10:]

stacks = {}

for columnn in range(1, columns+1):
    #get index value of current column number to determine position of box on each line
    column_index = content[8].index(str(columnn))

    for line in cargo_lines[::-1]:
        if not stacks.get(columnn):
            stacks[columnn] = []
        #if there is letter on that index, add it to stacks
        if line[column_index] != " ":
            stacks[columnn].append(line[column_index])

#create a copy to work with
#using deepcopy instead of .copy() - copy() would create shallow copy only..
stacks_pt1 = deepcopy(stacks)
stacks_pt2 = deepcopy(stacks)


def move(stack, count, fromColumn, toColumn, reverse=True):
    #print(f"moving {count} from {fromColumn} to {toColumn}")

    items_to_move = stack[fromColumn][-count:]
    if reverse:
        items_to_move.reverse()

    stack[toColumn] += items_to_move
    #remove items from fromColumn
    stack[fromColumn] = stack[fromColumn][:-count]


for instruction in move_instructions:
    #parse move instruction
    values = [int(value) for value in instruction.split(' ') if value.isdigit()]
    move(stacks_pt1, *values)

result = ""

for stack in stacks_pt1.values():
    stack.reverse()
    result += stack[0]

print(result)

#pt 2

print(stacks_pt2)
for instruction in move_instructions:
    #parse move instruction
    values = [int(value) for value in instruction.split(' ') if value.isdigit()]
    move(stacks_pt2, *values, reverse=False)

result2 = ""
for stack in stacks_pt2.values():
    stack.reverse()
    result2 += stack[0]

print(result2)