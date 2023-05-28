###############################################
# --- Day 13: Knights of the Dinner Table --- #
###############################################

import AOCUtils
from itertools import permutations

def get_max_happiness(relationships, attendees):
    max_happiness = 0
    for table in permutations(attendees):
        total_happiness = 0
        for i in range(len(table)):
            a, b = table[i-1], table[i]
            total_happiness += relationships[(a, b)]
            total_happiness += relationships[(b, a)]

        max_happiness = max(max_happiness, total_happiness)

    return max_happiness

###############################################

rawRelationships = AOCUtils.load_input(13)

relationships = dict()
for relationship in rawRelationships:
    relationship = relationship.split()

    a = relationship[0]
    b = relationship[-1][:-1]

    happiness = int(relationship[3])
    if relationship[2] == 'lose':
        happiness *= -1

    relationships[(a, b)] = happiness

attendees = set(a for a, _ in relationships)

AOCUtils.print_answer(1, get_max_happiness(relationships, attendees))

myself = 'Myself'
for attendee in attendees:
    relationships[(attendee, myself)] = 0
    relationships[(myself, attendee)] = 0
attendees.add(myself)

AOCUtils.print_answer(2, get_max_happiness(relationships, attendees))

AOCUtils.print_time_taken()