###############################################
# --- Day 12: Subterranean Sustainability --- #
###############################################

import AOCUtils

MARGIN = 100
GENAMT = 200

def getSumPots(gen):
    return sum(i-MARGIN for i in range(len(gen)) if gen[i] == "#")

###############################################

rawInput = AOCUtils.loadInput(12)

initial = rawInput[0].split()[2]
rules = dict()
for rule in rawInput[2:]:
    r = rule.split()
    rules[r[0]] = r[2]

generations = []
cur = "."*MARGIN + initial + "."*MARGIN
generations.append(cur)

genLen = len(cur)
for i in range(GENAMT):
    nextGen = ["." for _ in range(genLen)]
    for i in range(2, genLen-2):
        nextGen[i] = rules[cur[i-2:i+3]]
    generations.append(nextGen)
    cur = "".join(nextGen)

sumPots = [getSumPots(generations[i]) for i in range(GENAMT)]

print("Part 1: {}".format(sumPots[20]))

delta = sumPots[1] - sumPots[0]
for i in range(2, GENAMT-1):
    newDelta = sumPots[i] - sumPots[i-1]
    if delta == newDelta:
        print("Part 2: {}".format(sumPots[i] + delta*(50000000000-i)))
        break
    else:
        delta = newDelta

AOCUtils.printTimeTaken()