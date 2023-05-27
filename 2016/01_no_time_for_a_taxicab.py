########################################
# --- Day 1: No Time for a Taxicab --- #
########################################

import AOCUtils

########################################

steps = AOCUtils.loadInput(1)
steps = [s.strip() for s in steps.split(",")]

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # NESW, clockwise

pos = (0, 0)
facing = 0
visited = set()
hq = None
for step in steps:
    d, n = step[0], int(step[1:])

    facing += 1 if d == "R" else -1
    direction = directions[facing%4]

    for _ in range(n):
        pos = (pos[0]+direction[0], pos[1]+direction[1])
        if not hq:
            if pos not in visited:
                visited.add(pos)
            else:
                hq = pos

distance = abs(pos[0]) + abs(pos[1])
print("Part 1: {}".format(distance))

distance = abs(hq[0]) + abs(hq[1])
print("Part 2: {}".format(distance))

AOCUtils.printTimeTaken()