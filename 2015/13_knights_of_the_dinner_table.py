###############################################
# --- Day 13: Knights of the Dinner Table --- #
###############################################

import AOCUtils
from itertools import permutations

def getMaxHappiness(relationships, attendees):
    maxHappiness = 0
    for table in permutations(attendees):
        totalHappiness = 0
        for i in range(len(table)):
            a, b = table[i-1], table[i]
            totalHappiness += relationships[(a, b)]
            totalHappiness += relationships[(b, a)]

        maxHappiness = max(maxHappiness, totalHappiness)

    return maxHappiness

###############################################

rawRelationships = AOCUtils.loadInput(13)

relationships = dict()
for relationship in rawRelationships:
    relationship = relationship.split()

    a = relationship[0]
    b = relationship[-1][:-1]

    happiness = int(relationship[3])
    if relationship[2] == "lose":
        happiness *= -1

    relationships[(a, b)] = happiness

attendees = set(a for a, _ in relationships)

print("Part 1: {}".format(getMaxHappiness(relationships, attendees)))

myself = "Myself"
for attendee in attendees:
    relationships[(attendee, myself)] = 0
    relationships[(myself, attendee)] = 0
attendees.add(myself)

print("Part 2: {}".format(getMaxHappiness(relationships, attendees)))

AOCUtils.printTimeTaken()