##########################################################
# --- Day 5: A Maze of Twisty Trampolines, All Alike --- #
##########################################################

import AOCUtils

##########################################################

original_jumps = AOCUtils.load_input(5)

jumps = original_jumps[:]
cur = 0
total_jumps = 0
while 0 <= cur < len(jumps):
    nxt = cur + jumps[cur]
    jumps[cur] += 1

    cur = nxt
    total_jumps += 1

AOCUtils.print_answer(1, total_jumps)

jumps = original_jumps[:]
cur = 0
total_jumps = 0
while 0 <= cur < len(jumps):
    nxt = cur + jumps[cur]
    jumps[cur] += 1 if jumps[cur] < 3 else -1

    cur = nxt
    total_jumps += 1

AOCUtils.print_answer(2, total_jumps)

AOCUtils.print_time_taken()