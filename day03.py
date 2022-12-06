import numpy as np

with open("day03.txt", 'r') as file:
    backpacks = [item.replace('\n', '') for item  in file.readlines()]

#split each backpack into compartments - basically two halves of same size
backpacks_compartments = [[backpack[:int(len(backpack)/2)], backpack[int(len(backpack)/2):]] for backpack in backpacks]

#pt 1

#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
def get_priority(item):
    if item.islower():
        priority = ord(item) - 96
    else:
        priority = ord(item) - 38

    print(f"{item} priority - {priority}")

    return priority

result = 0 
for backpack in backpacks_compartments:
    # ignore duplicate items
    for item in set(backpack[0]):
        if item in backpack[1]:
            print(f"item {item} in both {backpack[0]} and {backpack[1]}")
            result += get_priority(item)

print(result)

#pt 2

#split elves into groups of 3
group_size = 3
elf_groups = [backpacks[i:i + group_size] for i in range(0, len(backpacks), group_size)]

result2 = 0 
for backpacks in elf_groups:
    # ignore duplicate items
    for item in set(backpacks[0]):
        if item in backpacks[1] and item in backpacks[2]:
            print(f"item {item} in all three backpacks - {backpacks[0]}, {backpacks[1]} and {backpacks[2]}")
            result2 += get_priority(item)

print(result2)
