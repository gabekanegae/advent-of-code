###########################################
# --- Day 24: It Hangs in the Balance --- #
###########################################

import AOCUtils
from itertools import combinations

def get_quantum_entanglement(packages, totalGroups):
    group_weight = sum(packages) // totalGroups

    def divide(packages, groups):
        for i in range((len(packages) // groups) + 1):
            for group1 in combinations(packages, i):
                if sum(group1) != group_weight: continue

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

packages = AOCUtils.load_input(24)

AOCUtils.print_answer(1, get_quantum_entanglement(packages, 3))

AOCUtils.print_answer(2, get_quantum_entanglement(packages, 4))

AOCUtils.print_time_taken()