#####################################
# --- Day 9: Mirage Maintenance --- #
#####################################

import AOCUtils

def predict(l):
    if all(d == 0 for d in l):
        return 0

    deltas = [b - a for a, b in zip(l, l[1:])]
    return l[-1] + predict(deltas)

#####################################

raw_history = AOCUtils.load_input(9)
history = [list(map(int, l.split())) for l in raw_history]

AOCUtils.print_answer(1, sum(predict(l) for l in history))
AOCUtils.print_answer(2, sum(predict(l[::-1]) for l in history))

AOCUtils.print_time_taken()
