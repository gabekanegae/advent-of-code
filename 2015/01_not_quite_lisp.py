#################################
# --- Day 1: Not Quite Lisp --- #
#################################

import AOCUtils

#################################

directions = AOCUtils.load_input(1)

directions = [1 if c == '(' else -1 for c in directions]

AOCUtils.print_answer(1, sum(directions))

cur = 0
for i, c in enumerate(directions):
    cur += c
    if cur == -1:
        AOCUtils.print_answer(2, i+1)
        break

AOCUtils.print_time_taken()