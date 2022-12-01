def max_calories_finder(lines, number_of_results=1):
    calorie_totals = []
    temp_sum = 0
    for line in lines:
        if(line != ''):
            temp_sum += int(line,10)
        else:
            calorie_totals.append(temp_sum)
            temp_sum = 0
    
    results = []
    for _ in range(number_of_results):
        result = max(calorie_totals)
        results.append(result)
        calorie_totals.remove(result)
        
    return sum(results)


file = open('input.txt')
lines = map(lambda l: l.strip() ,file.readlines())
print(max_calories_finder(lines,3))

