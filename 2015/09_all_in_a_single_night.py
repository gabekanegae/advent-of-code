########################################
# --- Day 9: All in a Single Night --- #
########################################

import AOCUtils
from collections import deque
from itertools import permutations

########################################

rawDistances = AOCUtils.loadInput(9)

locations = set()
distances = dict()
for rawDist in rawDistances:
    rawDist = rawDist.split()
    a, b = rawDist[0], rawDist[2]
    dist = int(rawDist[4])

    distances[(a, b)] = dist
    distances[(b, a)] = dist

    locations.add(a)
    locations.add(b)

minDist, maxDist = None, None
for order in permutations(locations):
    dist = 0

    for i in range(1, len(order)):
        dist += distances[(order[i-1], order[i])]

    minDist = min(minDist, dist) if minDist else dist
    maxDist = max(maxDist, dist) if maxDist else dist

print("Part 1: {}".format(minDist))

print("Part 2: {}".format(maxDist))

AOCUtils.printTimeTaken()