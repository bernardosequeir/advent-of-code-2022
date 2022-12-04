def get_item_priority(item): 
    if(item >= 'a' and item <= 'z'):
        return ord(item) - ord('a') + 1
    elif(item >= 'A' and item <= 'Z'):
        return ord(item) - ord('A') + 27
    else: 
        return 0

def get_repeated_priority(rucksacks):
    priority_sum = 0
    rucksack_compartments = []
    
    for rucksack in rucksacks:
        rucksack_compartments.append([rucksack[0:int(len(rucksack) / 2)], rucksack[int(len(rucksack)/ 2):]])
    
    for compartments in rucksack_compartments:
        first, second = compartments
        
        for item in set(first): 
            priority_sum += get_item_priority(item) if second.find(item) > -1 else 0
    
    return priority_sum
        
def get_group_repeated_priority(rucksacks):
    priority_sum = 0
    groups = []

    for idx in range(0, len(rucksacks), 3):
        groups.append([rucksacks[idx], rucksacks[idx + 1], rucksacks[idx + 2]])

    for group in groups:
        first, second, third = group
        
        for item in set(first):
            priority_sum += get_item_priority(item) if second.find(item) > -1 and third.find(item) > -1 else 0
    
    return priority_sum
     

file = open('input.txt')
lines = [l.strip() for l in file.readlines()]
print(get_repeated_priority(lines))
print(get_group_repeated_priority(lines))