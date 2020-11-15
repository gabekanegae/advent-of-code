###########################################
# --- Day 24: It Hangs in the Balance --- #
###########################################

import AOCUtils
from itertools import combinations

def getQuantumEntanglement(packages, totalGroups):
    groupWeight = sum(packages) // totalGroups

    def divide(packages, groups):
        for i in range((len(packages) // groups) + 1):
            for group1 in combinations(packages, i):
                if sum(group1) != groupWeight: continue

                qe = 1
                for w in group1:
                    qe *= w

                if groups == 1:
                    return qe

                remaining = list(set(packages) - set(group1))

                if groups < totalGroups:
                    return divide(remaining, groups-1)
                
                if divide(remaining, groups-1) != 0:
                    return qe

    return divide(packages, totalGroups)

###########################################

packages = AOCUtils.loadInput(24)

print("Part 1: {}".format(getQuantumEntanglement(packages, 3)))

print("Part 2: {}".format(getQuantumEntanglement(packages, 4)))

AOCUtils.printTimeTaken()