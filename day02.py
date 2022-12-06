with open("day02.txt", 'r') as file:
    content = [item.replace('\n', '') for item  in file.readlines()]

rounds = [item.split(" ") for item in content]

#pt 1
def evaluate_result(p1_choice, p2_choice):
    result = 0

    p1 = None
    p2 = None

    match p1_choice:
        case "A":
            p1 = 1
        case "B":
            p1 = 2
        case "C":
            p1 = 3 

    match p2_choice:
        case "X":
            p2 = 1
        case "Y":
            p2 = 2
        case "Z":
            p2 = 3

    if not p1 or not p2:   
        print("Unknown player choice")
        return
        
    if p1 == p2:
        #draw
        return p2 + 3
    elif (p2 - p1 == 1) or (p1 - p2 == 2):
        #p2 wins
        return p2 + 6
    else:
        return p2

#print(rounds)

rslt = 0

for r in rounds:
    rslt += evaluate_result(r[0], r[1])

print("final points p1 1: ", rslt)

#pt 2

def evaluate_expected_result(p1_choice, expected_outcome):
    result = 0

    p1 = None

    match p1_choice:
        case "A":
            p1 = 1
        case "B":
            p1 = 2
        case "C":
            p1 = 3 

    match expected_outcome:
        case "X":
            # lose
            if p1 in [2,3]:
                # if p1 choice is paper (2) or scissors (3) choose p1 - 1 to lose
                result += p1 - 1
            else:
                # if p1 choice is rock (1) choose scissors (3) to lose
                result += 3
        case "Y":
            # draw
            # return p1 choice value + 3 points for draw
            result += p1 + 3
        case "Z":
            # win
            # add 6 points for win
            result += 6
            if p1 in [1,2]:
                # if p1 choice is rock (1) or paper (2) choose p1 + 1
                result += p1 + 1
            else:
                # if p1 choice is scissors (3) choose rock (1) to win 
                result += 1

    return result


rslt2 = 0

for r in rounds:
    rslt2 += evaluate_expected_result(r[0], r[1])

print("final points p1 2: ", rslt2)