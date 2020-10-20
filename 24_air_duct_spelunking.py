#######################################
# --- Day 24: Air Duct Spelunking --- #
#######################################

import AOCUtils
from collections import deque
from itertools import permutations

#######################################

ducts = AOCUtils.loadInput(24)

points = dict()
for x in range(len(ducts)):
    for y in range(len(ducts[0])):
        if ducts[x][y] in "0123456789":
            points[ducts[x][y]] = (x, y)

# Get minimum distance from all points to all points
allDistances = dict()
for a, start in points.items():
    for b, dest in points.items():
        if (b, a) in allDistances:
            allDistances[(a, b)] = allDistances[(b, a)]
            continue
        if a == b:
            allDistances[(a, b)] = 0
            continue

        queue = deque([(start, 0)])
        visited = set()
        while queue:
            cur, dist = queue.popleft()

            if cur in visited: continue
            visited.add(cur)

            # Optimization (not worth it for this problem size, might be good for larger maps):
            # If it's computing a->b and it's at c and c->b has already been computed, a->b = a->c + c->b
            # c = ducts[cur[0]][cur[1]]
            # if c in "0123456789":
            #     if (c, b) in allDistances:
            #         dist += allDistances[(c, b)]
            #         if (a, b) not in allDistances or dist < allDistances[(a, b)]:
            #             allDistances[(a, b)] = dist
            #         continue

            if cur == dest:
                allDistances[(a, b)] = dist
                break

            for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nxt = (cur[0]+move[0], cur[1]+move[1])
                if ducts[nxt[0]][nxt[1]] != "#":
                    queue.append((nxt, dist+1))

dests = set(points.keys())
dests.remove("0")

minDist = None
for order in permutations(dests):
    order = "0" + "".join(order)
    dist = 0
    for i in range(1, len(order)):
        dist += allDistances[(order[i-1], order[i])]
    minDist = min(minDist, dist) if minDist else dist

print("Part 1: {}".format(minDist))

minDist = None
for order in permutations(dests):
    order = "0" + "".join(order) + "0"
    dist = 0
    for i in range(1, len(order)):
        dist += allDistances[(order[i-1], order[i])]
    minDist = min(minDist, dist) if minDist else dist

print("Part 2: {}".format(minDist))

AOCUtils.printTimeTaken()