########################################
# --- Day 9: All in a Single Night --- #
########################################

import AOCUtils
from collections import deque
from itertools import permutations

########################################

raw_distances = AOCUtils.load_input(9)

locations = set()
distances = dict()
for raw_dist in raw_distances:
    raw_dist = raw_dist.split()
    a, b = raw_dist[0], raw_dist[2]
    dist = int(raw_dist[4])

    distances[(a, b)] = dist
    distances[(b, a)] = dist

    locations.add(a)
    locations.add(b)

min_dist, max_dist = None, None
for order in permutations(locations):
    dist = 0

    for i in range(1, len(order)):
        dist += distances[(order[i-1], order[i])]

    min_dist = min(min_dist, dist) if min_dist else dist
    max_dist = max(max_dist, dist) if max_dist else dist

AOCUtils.print_answer(1, min_dist)

AOCUtils.print_answer(2, max_dist)

AOCUtils.print_time_taken()