##################################
# --- Day 22: Grid Computing --- #
##################################

import AOCUtils
from collections import deque

##################################

rawNodes = AOCUtils.loadInput(22)[2:]

nodes = dict()
for rawNode in rawNodes:
    rawNode = rawNode.split()
    
    name, size, used, avail, pct = rawNode
    x, y = name.split("-")[1:]

    x, y = int(x[1:]), int(y[1:])
    size, used = int(size[:-1]), int(used[:-1])
    avail, pct = int(avail[:-1]), int(pct[:-1])

    nodes[(x, y)] = {"size": size, "used": used, "avail": avail, "pct": pct}

viableCount = 0
for a in nodes:
    for b in nodes:
        if a == b: continue

        if nodes[a]["used"] != 0 and nodes[a]["used"] < nodes[b]["avail"]:
            viableCount += 1

print("Part 1: {}".format(viableCount))

goal = (max(p[0] for p in nodes), 0)

# Assume nodes follow the same three categories from the example
empty = None
for node in nodes:
    if node == goal:
        nodes[node] = "G"
    elif nodes[node]["size"] > 100: # "very large, very full node"
        nodes[node] = "#"
    elif nodes[node]["used"] == 0: # "empty node"
        nodes[node] = "_"
        empty = node
    else:# "full enough no other node would fit, small enough to be moved around"
        nodes[node] = "."

# for y in range(max(p[1] for p in nodes)+1):
#     for x in range(max(p[0] for p in nodes)+1):
#         print(nodes[(x,y)], end="")
#     print()

# Get steps required to move empty node to the left of G
dest = (goal[0]-1, goal[1])
queue = deque([(empty, 0)])
visited = set()
while queue:
    cur, dist = queue.popleft()

    if cur in visited: continue
    visited.add(cur)

    if cur == dest: break

    for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        nxt = (cur[0]+move[0], cur[1]+move[1])
        if 0 <= nxt[0] <= maxX and 0 <= nxt[1] <= maxY:
            if nodes[nxt] == ".":
                queue.append((nxt, dist+1))

# Grid y=0 state:    .....[...]...._G
# 1 step to become:  .....[...]....G_
# 5 steps to become: .....[...]...G_.
# 5 steps to become: .....[...]..G_..
# ...and so on

totalDist = dist + 1 + cur[0] * 5
print("Part 1: {}".format(totalDist))

AOCUtils.printTimeTaken()