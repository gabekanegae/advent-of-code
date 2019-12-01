######################################
# --- Day 1: Chronal Calibration --- #
######################################

import AOCUtils

######################################

freqs = AOCUtils.loadInput(1)

print("Part 1: {}".format(sum(freqs)))

history = set()
curFreq = 0
i = 0
while True:
    curFreq += freqs[i%len(freqs)]
    if curFreq in history:
        break
    else:
        history.add(curFreq)
        i += 1

print("Part 2: {}".format(curFreq))

AOCUtils.printTimeTaken()