######################################
# --- Day 6: Memory Reallocation --- #
######################################

import AOCUtils

######################################

banks = AOCUtils.load_input(6)

seen = {tuple(banks): 0}

while True:
    most = 0
    for i in range(1, len(banks)):
        if banks[i] > banks[most]:
            most = i

    distribute = banks[most]
    banks[most] = 0
    cur = most + 1
    for i in range(distribute):
        banks[cur%len(banks)] += 1
        cur += 1

    new = tuple(banks)
    if new in seen:
        break
    seen[new] = len(seen)

AOCUtils.print_answer(1, len(seen))

AOCUtils.print_answer(2, len(seen) - seen[new])

AOCUtils.print_time_taken()