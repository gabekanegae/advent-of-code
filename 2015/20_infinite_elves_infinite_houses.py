######################################################
# --- Day 20: Infinite Elves and Infinite Houses --- #
######################################################

import AOCUtils

max_houses = 1000000

######################################################

presents = AOCUtils.load_input(20)

houses = dict()
for elf in range(1, presents):
    limit = max_houses
    for house in range(elf, limit, elf):
        if house not in houses:
            houses[house] = 0
        houses[house] += 10 * elf

    if houses[elf] >= presents:
        AOCUtils.print_answer(1, elf)
        break

houses = dict()
for elf in range(1, presents):
    limit = min(50 * elf, max_houses)
    for house in range(elf, limit, elf):
        if house not in houses:
            houses[house] = 0
        houses[house] += 11 * elf

    if houses[elf] >= presents:
        AOCUtils.print_answer(2, elf)
        break

AOCUtils.print_time_taken()