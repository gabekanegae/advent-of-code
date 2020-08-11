####################################################
# --- Day 13: A Maze of Twisty Little Cubicles --- #
####################################################

import AOCUtils
from collections import deque

def getTile(fav, p):
    x, y = p

    n = x*x + 3*x + 2*x*y + y + y*y
    n += fav

    setBits = 0
    while n:
        setBits += n % 2
        n //= 2

    return "#" if setBits % 2 == 1 else "."

####################################################

fav = AOCUtils.loadInput(13)

goal = (31, 39)

visited = set()
queue = deque([((1, 1), 0)])
while queue:
    cur, curDist = queue.popleft()

    if cur in visited: continue
    visited.add(cur)

    if cur == goal:
        break

    for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nxt = (cur[0] + delta[0], cur[1] + delta[1])

        if nxt[0] >= 0 and nxt[1] >= 0 and getTile(fav, nxt) == ".":
            queue.append((nxt, curDist+1))

print("Part 1: {}".format(curDist))

visited = set()
queue = deque([((1, 1), 0)])
while queue:
    cur, curDist = queue.popleft()

    if cur in visited: continue
    visited.add(cur)

    if curDist == 50:
        continue

    for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nxt = (cur[0] + delta[0], cur[1] + delta[1])

        if nxt[0] >= 0 and nxt[1] >= 0 and getTile(fav, nxt) == ".":
            queue.append((nxt, curDist+1))

print("Part 2: {}".format(len(visited)))

AOCUtils.printTimeTaken()