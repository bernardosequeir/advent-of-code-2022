def get_match_value(values):
    score = 0
    if(values[0] == 'A'):
        if(values[1] == 'X'):
            score += 4
        elif(values[1] == 'Y'):
            score += 8
        elif(values[1] == 'Z'):
            score += 3
    elif(values[0] == 'B'):
        if(values[1] == 'X'):
            score += 1
        elif(values[1] == 'Y'):
            score += 5
        elif(values[1] == 'Z'):
            score += 9
    elif(values[0] == 'C'):
        if(values[1] == 'X'):
            score += 7
        elif(values[1] == 'Y'):
            score += 2
        elif(values[1] == 'Z'):
            score += 6
    return score
    
def get_match_value_part2(values):
    score = 0
    if(values[0] == 'A'):
        if(values[1] == 'X'):
            score += 3
        elif(values[1] == 'Y'):
            score += 4
        elif(values[1] == 'Z'):
            score += 8
    elif(values[0] == 'B'):
        if(values[1] == 'X'):
            score += 1
        elif(values[1] == 'Y'):
            score += 5
        elif(values[1] == 'Z'):
            score += 9
    elif(values[0] == 'C'):
        if(values[1] == 'X'):
            score += 2
        elif(values[1] == 'Y'):
            score += 6
        elif(values[1] == 'Z'):
            score += 7
    return score
   


def score_finder(matches, calculator):
    total_score = 0
    for match in matches: 
        total_score += calculator(match)
    return(total_score)


file = open('input.txt')
lines = [l.strip() for l in file.readlines()]
matches = []
for line in lines: 
    matches.append(line.split(' '))
print(score_finder(matches, get_match_value))
print(score_finder(matches, get_match_value_part2))

