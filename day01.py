#pt 1
with open("day01.txt", 'r') as file:
    inventory = [item.replace('\n', '') for item  in file.readlines()]

current_elf = []
elves = []

#print(inventory)

for i in inventory:
    if i == '':
        elves.append(current_elf)
        current_elf = []
        continue
    current_elf.append(int(i))

elves_sumed = [sum(elf) for elf in elves]
print(max(elves_sumed))

#pt 2
print(sum(sorted(elves_sumed)[-3:]))