######################################
# --- Day 1: Chronal Calibration --- #
######################################

import AOCUtils

######################################

freqs = AOCUtils.load_input(1)

AOCUtils.print_answer(1, sum(freqs))

history = set()
freq = 0
i = 0
while True:
    freq += freqs[i%len(freqs)]
    if freq not in history:
        history.add(freq)
        i += 1
    else:
        break

AOCUtils.print_answer(2, freq)

AOCUtils.print_time_taken()