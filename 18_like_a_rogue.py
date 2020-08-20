################################
# --- Day 18: Like a Rogue --- #
################################

import AOCUtils

def getSafeTiles(curRow, n):
    curRow = list(curRow)
    traps = set(["^^.", ".^^", "^..", "..^"])

    safeTiles = 0
    for _ in range(n):
        safeTiles += curRow.count(".")

        newRow = []
        for i in range(len(curRow)):
            l = curRow[i-1] if i-1 >= 0 else "."
            c = curRow[i]
            r = curRow[i+1] if i+1 < len(curRow) else "."

            s = "^" if "".join([l, c, r]) in traps else "."
            newRow.append(s)

        curRow = newRow

    return safeTiles@

################################

curRow = AOCUtils.loadInput(18)

print("Part 1: {}".format(getSafeTiles(curRow, 40)))

print("Part 2: {}".format(getSafeTiles(curRow, 400000)))

AOCUtils.printTimeTaken()