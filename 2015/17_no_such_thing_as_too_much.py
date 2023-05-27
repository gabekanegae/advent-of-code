#############################################
# --- Day 17: No Such Thing as Too Much --- #
#############################################

import AOCUtils
from itertools import combinations

#############################################

containers = AOCUtils.loadInput(17)
eggnog = 150

containerAmounts = []
for i in range(len(containers)+1):
    for combination in combinations(containers, i):
        if sum(combination) == eggnog:
            containerAmounts.append(i)

p1 = len(containerAmounts)
print("Part 1: {}".format(p1))

p2 = containerAmounts.count(min(containerAmounts))
print("Part 2: {}".format(p2))

AOCUtils.printTimeTaken()