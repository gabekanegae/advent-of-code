############################
# --- Day 17: Spinlock --- #
############################

import AOCUtils
from collections import deque

############################

step_amount = AOCUtils.load_input(17)

circle = deque([0])
for i in range(1, 2017+1):
    circle.rotate(-step_amount)
    circle.append(i)

AOCUtils.print_answer(1, circle[(circle.index(2017)+1) % len(circle)])

circle = deque([0])
for i in range(1, 500000+1):
    circle.rotate(-step_amount)
    circle.append(i)

AOCUtils.print_answer(2, circle[(circle.index(0)+1) % len(circle)])

AOCUtils.print_time_taken()