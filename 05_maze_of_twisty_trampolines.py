##########################################################
# --- Day 5: A Maze of Twisty Trampolines, All Alike --- #
##########################################################

import AOCUtils

##########################################################

origJumps = AOCUtils.loadInput(5)

jumps = origJumps[:]
cur = 0
totalJumps = 0
while 0 <= cur < len(jumps):
    newCur = cur + jumps[cur]
    jumps[cur] += 1

    cur = newCur
    totalJumps += 1

print("Part 1: {}".format(totalJumps))

jumps = origJumps[:]
cur = 0
totalJumps = 0
while 0 <= cur < len(jumps):
    newCur = cur + jumps[cur]
    jumps[cur] += 1 if jumps[cur] < 3 else -1

    cur = newCur
    totalJumps += 1

print("Part 2: {}".format(totalJumps))

AOCUtils.printTimeTaken()