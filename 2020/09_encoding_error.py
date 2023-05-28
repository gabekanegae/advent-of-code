#################################
# --- Day 9: Encoding Error --- #
#################################

import AOCUtils
from itertools import combinations

#################################

data = AOCUtils.load_input(9)

for i in range(25, len(data)):
    if data[i] not in [sum(l) for l in combinations(data[i-25:i], 2)]:
        p1 = data[i]
        break

AOCUtils.print_answer(1, p1)

i = 0
j = 1
cum_sum = data[i]
while i < len(data):
    cum_sum += data[j] # cum_sum == sum(data[i:j+1])

    if cum_sum == p1:
        p2 = min(data[i:j+1]) + max(data[i:j+1])
        break

    if cum_sum > p1 or j == len(data) - 1:
        i += 1
        j = i
        cum_sum = data[i]

    j += 1

AOCUtils.print_answer(2, p2)

AOCUtils.print_time_taken()