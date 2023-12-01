##########################################
# --- Day 3: Rucksack Reorganization --- #
##########################################

import AOCUtils

def get_priority(item):
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 26 + 1

##########################################

rucksacks = AOCUtils.load_input(3)

sum_of_priorities = 0
for rucksack in rucksacks:
    middle = len(rucksack) // 2
    a, b = rucksack[:middle], rucksack[middle:]

    unique = set(a).intersection(set(b)).pop()
    sum_of_priorities += get_priority(unique)

AOCUtils.print_answer(1, sum_of_priorities)

elves = 3
rucksack_groups = [rucksacks[i:i+elves] for i in range(0, len(rucksacks), elves)]

sum_of_priorities = 0
for rucksack_group in rucksack_groups:
    unique = set.intersection(*map(set, rucksack_group))
    sum_of_priorities += get_priority(unique.pop())

AOCUtils.print_answer(2, sum_of_priorities)

AOCUtils.print_time_taken()