##########################
# --- Day 11: Hex Ed --- #
##########################

import AOCUtils

def distToOrigin(p):
    x, y = p
    if (x >= 0) == (y >= 0):
        return abs(x + y)
    else:
        return max(abs(x), abs(y))

##########################

path = AOCUtils.loadInput(11).split(",")

# X axis rotated 30 deg (L/R is SW/NE)
directions = {"nw": (-1, 1), "n": (0, 1), "ne": (1, 0),
              "sw": (-1, 0), "s": (0, -1), "se": (1, -1)}

steps = [(0, 0)]
for p in path:
    x, y = steps[-1]
    dx, dy = directions[p]
    steps.append((x+dx, y+dy))

print("Part 1: {}".format(distToOrigin(steps[-1])))
print("Part 2: {}".format(max(distToOrigin(step) for step in steps)))

AOCUtils.printTimeTaken()