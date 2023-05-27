########################################
# --- Day 15: Timing is Everything --- #
########################################

import AOCUtils

def timeDiscs(discs):
    t = 0
    while True:
        if all((t + idx + pos) % size == 0 for idx, size, pos in discs):
            return t
        t += 1

########################################

rawDiscs = AOCUtils.loadInput(15)

discs = []
for rawDisc in rawDiscs:
    rawDisc = rawDisc.split()

    idx = int(rawDisc[1][1:])
    size = int(rawDisc[3])
    pos = int(rawDisc[11][:-1])

    disc = (idx, size, pos)
    discs.append(disc)

print("Part 1: {}".format(timeDiscs(discs)))

newDisc = (len(discs)+1, 11, 0)
discs.append(newDisc)

print("Part 2: {}".format(timeDiscs(discs)))

AOCUtils.printTimeTaken()