#################################
# --- Day 1: Not Quite Lisp --- #
#################################

import AOCUtils

#################################

directions = AOCUtils.loadInput(1)

directions = [1 if c == "(" else -1 for c in directions]

print("Part 1: {}".format(sum(directions)))

cur = 0
for i, c in enumerate(directions):
    cur += c
    if cur == -1:
        print("Part 2: {}".format(i+1))
        break

AOCUtils.printTimeTaken()