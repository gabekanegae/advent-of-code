########################################
# --- Day 15: Timing is Everything --- #
########################################

import AOCUtils

def time_discs(discs):
    t = 0
    while True:
        if all((t + idx + pos) % size == 0 for idx, size, pos in discs):
            return t
        t += 1

########################################

raw_discs = AOCUtils.load_input(15)

discs = []
for raw_disc in raw_discs:
    raw_disc = raw_disc.split()

    idx = int(raw_disc[1][1:])
    size = int(raw_disc[3])
    pos = int(raw_disc[11][:-1])

    disc = (idx, size, pos)
    discs.append(disc)

AOCUtils.print_answer(1, time_discs(discs))

new_disc = (len(discs)+1, 11, 0)
discs.append(new_disc)

AOCUtils.print_answer(2, time_discs(discs))

AOCUtils.print_time_taken()