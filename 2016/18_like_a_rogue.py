################################
# --- Day 18: Like a Rogue --- #
################################

import AOCUtils

def getSafeTiles(cur, n):
    cur = list(cur)

    safeTiles = 0
    for _ in range(n):
        safeTiles += cur.count(".")

        nxt = []
        for i in range(len(cur)):
            l = cur[i-1] if i-1 >= 0 else "."
            r = cur[i+1] if i+1 < len(cur) else "."

            nxt.append("^" if l != r else ".")

        cur = nxt

    return safeTiles

################################

cur = AOCUtils.loadInput(18)

print("Part 1: {}".format(getSafeTiles(cur, 40)))

print("Part 2: {}".format(getSafeTiles(cur, 400000)))

AOCUtils.printTimeTaken()