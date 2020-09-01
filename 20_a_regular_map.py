#################################
# --- Day 20: A Regular Map --- #
#################################

import AOCUtils

#################################

regexp = AOCUtils.loadInput(20)[1:-1]
maxBound = len(regexp)

stack = []
pos = (maxBound, maxBound)
roomDistances = {pos: 0}

moves = {"N": (0, -1), "W": (-1, 0), "S": (0, 1), "E": (1, 0)}
for c in regexp:
    lastPos = pos

    if c == "(":
        stack.append(pos)
    elif c == ")":
        pos = stack.pop()
    elif c == "|":
        pos = stack[-1]
    else: # NWSE
        delta = moves[c]
        pos = (pos[0]+delta[0], pos[1]+delta[1])
        if pos in roomDistances:
            roomDistances[pos] = min(roomDistances[pos], roomDistances[lastPos] + 1)
        else:
            roomDistances[pos] = roomDistances[lastPos] + 1

print("Part 1: {}".format(max(roomDistances.values())))

farRooms = sum(dist >= 1000 for dist in roomDistances.values())
print("Part 2: {}".format(farRooms))

AOCUtils.printTimeTaken()