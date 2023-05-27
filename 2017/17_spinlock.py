############################
# --- Day 17: Spinlock --- #
############################

import AOCUtils
from collections import deque

############################

stepAmt = AOCUtils.loadInput(17)

circle = deque([0])
for i in range(1, 2017+1):
    circle.rotate(-stepAmt)
    circle.append(i)

print(circle[(circle.index(2017)+1) % len(circle)])

circle = deque([0])
for i in range(1, 500000+1):
    circle.rotate(-stepAmt)
    circle.append(i)

print(circle[(circle.index(0)+1) % len(circle)])

AOCUtils.printTimeTaken()