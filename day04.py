with open("day04.txt", 'r') as file:
    range_pairs = [item.replace('\n', '').split(",") for item  in file.readlines()]


#pt 1
result = 0

for range_pair in range_pairs:

    n1, n2 = range_pair[0].split("-")
    n3, n4 = range_pair[1].split("-")
    print(n1, n2)
    print(n3, n4)

    range1 = [i for i in range(int(n1), int(n2)+1)]
    range2 = [i for i in range(int(n3), int(n4)+1)]
    print(range1)
    print(range2)

    if all(num in range1 for num in range2) or all(num in range2 for num in range1):
        result += 1

print(result)

#pt 2
result2 = 0

for range_pair in range_pairs:

    n1, n2 = range_pair[0].split("-")
    n3, n4 = range_pair[1].split("-")

    range1 = [i for i in range(int(n1), int(n2)+1)]
    range2 = [i for i in range(int(n3), int(n4)+1)]


    if any(num in range1 for num in range2) or any(num in range2 for num in range1):
        result2 += 1

print(result2)