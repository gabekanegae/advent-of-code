#############################################
# --- Day 17: No Such Thing as Too Much --- #
#############################################

import AOCUtils
from itertools import combinations

#############################################

containers = AOCUtils.load_input(17)
eggnog = 150

container_amounts = []
for i in range(len(containers)+1):
    for combination in combinations(containers, i):
        if sum(combination) == eggnog:
            container_amounts.append(i)

AOCUtils.print_answer(1, len(container_amounts))

AOCUtils.print_answer(2, container_amounts.count(min(container_amounts)))

AOCUtils.print_time_taken()