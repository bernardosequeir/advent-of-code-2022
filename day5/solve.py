import re


def sort_crates_9000(instructions):
    stacks = [
        ["W", "B", "D", "N", "C", "F", "J"],
        ["P", "Z", "V", "Q", "L", "S", "T"],
        ["P", "Z", "B", "G", "J", "T"],
        ["D", "T", "L", "J", "Z", "B", "H", "C"],
        ["G", "V", "B", "J", "S"],
        ["P", "S", "Q"],
        ["B", "V", "D", "F", "L", "M", "P", "N"],
        ["P", "S", "M", "F", "B", "D", "L", "R"],
        ["V", "D", "T", "R"]
    ]
    
    for instruction in instructions:
        qty, src, dest = [int(i) for i in instruction]
        moved_crates = stacks[src-1][-qty:]
        moved_crates.reverse()
        del stacks[src-1][-qty:]
        stacks[dest-1].extend(moved_crates)
    return ''.join([stack[-1] for stack in stacks])

def sort_crates_9001(instructions):
    stacks = [
        ["W", "B", "D", "N", "C", "F", "J"],
        ["P", "Z", "V", "Q", "L", "S", "T"],
        ["P", "Z", "B", "G", "J", "T"],
        ["D", "T", "L", "J", "Z", "B", "H", "C"],
        ["G", "V", "B", "J", "S"],
        ["P", "S", "Q"],
        ["B", "V", "D", "F", "L", "M", "P", "N"],
        ["P", "S", "M", "F", "B", "D", "L", "R"],
        ["V", "D", "T", "R"]
    ]
    
    for instruction in instructions:
        qty, src, dest = [int(i) for i in instruction]
        moved_crates = stacks[src-1][-qty:]
        del stacks[src-1][-qty:]
        stacks[dest-1].extend(moved_crates)
    return ''.join([stack[-1] for stack in stacks]) 

file = open('input.txt')
lines = [re.findall(r'\b\d+\b', l) for l in file.readlines()]
print(sort_crates_9000(lines))
print(sort_crates_9001(lines))
