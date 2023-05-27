#####################################
# --- Day 17: Two Steps Forward --- #
#####################################

import AOCUtils
import hashlib
from collections import deque

#####################################

passcode = AOCUtils.loadInput(17)

baseDigest = hashlib.md5(passcode.encode())

moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
end = (3, 3)

minPath = None
maxPathLen = 0

queue = deque([((0, 0), [])])
while queue:
    cur, path = queue.popleft()

    if cur == end:
        minPath = minPath or "".join(path)
        maxPathLen = max(maxPathLen, len(path))
        continue

    digest = baseDigest.copy()
    digest.update("".join(path).encode())
    s = digest.hexdigest()

    for i, (p, d) in enumerate(moves.items()):
        if int(s[i], 16) > 10: # bcdef
            nxt = (cur[0]+d[0], cur[1]+d[1])
            if 0 <= nxt[0] <= 3 and 0 <= nxt[1] <= 3:
                queue.append((nxt, path+[p]))

print("Part 1: {}".format(minPath))

print("Part 2: {}".format(maxPathLen))

AOCUtils.printTimeTaken()