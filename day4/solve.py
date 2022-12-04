def is_range_completely_inside_range(r): 
    [r1,r2,r3,r4] = [int(x) for x in r]
    return (r3 in range(r1, r2 +1) and r4 in range(r1, r2+1) or r1 in range(r3, r4+1) and r2 in range(r3, r4+1))

def is_range_overlapping_range(r): 
    [r1,r2,r3,r4] = [int(x) for x in r]
    return (r3 in range(r1, r2 +1) or r4 in range(r1, r2+1) or r1 in range(r3, r4+1) or r2 in range(r3, r4+1))

def get_overlap_count(groups, compare_fn = is_range_completely_inside_range):
    ranges = []
    overlap_count = 0
    for group in groups:
        group_ranges = [] 
        elves = group.split(',')
        for elf in elves:
            group_ranges.extend(elf.split('-'))
        ranges.append(group_ranges)
        overlap_count += 1 if compare_fn(group_ranges) else 0
    return overlap_count
    


file = open('input.txt')
lines = [l.strip() for l in file.readlines()]
print(get_overlap_count(lines, is_range_completely_inside_range))
print(get_overlap_count(lines, is_range_overlapping_range))
