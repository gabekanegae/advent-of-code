#############################################
# --- Day 17: No Such Thing as Too Much --- #
#############################################

import AOCUtils
from itertools import combinations

#############################################

containers = AOCUtils.load_input(17)
eggnog = 150

containerAmounts = []
for i in range(len(containers)+1):
    for combination in combinations(containers, i):
        if sum(combination) == eggnog:
            containerAmounts.append(i)

AOCUtils.print_answer(1, len(containerAmounts))

AOCUtils.print_answer(2, containerAmounts.count(min(containerAmounts)))

AOCUtils.print_time_taken()