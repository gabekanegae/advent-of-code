######################################################
# --- Day 20: Infinite Elves and Infinite Houses --- #
######################################################

import AOCUtils

maxHouses = 1000000

######################################################

presents = AOCUtils.loadInput(20)

houses = dict()
for elf in range(1, presents):
    limit = maxHouses
    for house in range(elf, limit, elf):
        if house not in houses:
            houses[house] = 0
        houses[house] += 10 * elf

    if houses[elf] >= presents:
        print("Part 1: {}".format(elf))
        break

houses = dict()
for elf in range(1, presents):
    limit = min(50 * elf, maxHouses)
    for house in range(elf, limit, elf):
        if house not in houses:
            houses[house] = 0
        houses[house] += 11 * elf

    if houses[elf] >= presents:
        print("Part 2: {}".format(elf))
        break

AOCUtils.printTimeTaken()