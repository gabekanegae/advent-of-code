##########################################################
# --- Day 11: Radioisotope Thermoelectric Generators --- #
##########################################################

import AOCUtils
from collections import deque

def assemble(floors, floorAmt):
    items = dict()
    for i, floor in enumerate(floors):
        for item in floor:
            mat, obj = item.split()
            mat = mat.split("-")[0]
            obj = "MG".index(obj[0].upper())

            if mat not in items:
                items[mat] = [None, None]
            items[mat][obj] = i

    visited = set()

    start = (0, tuple(sorted(tuple(items[mat]) for mat in items)))
    queue = deque([(start, 0)])
    while queue:
        curState, dist = queue.popleft()

        if curState in visited: continue
        visited.add(curState)

        curFloor, curItems = curState

        # All items are at the last floor
        if all(item == (floorAmt-1, floorAmt-1) for item in curItems):
            return dist

        ms = [mat[0] for mat in curItems]
        gs = [mat[1] for mat in curItems]

        # Check if any chips are fried
        fried = False
        for i, m in enumerate(ms):
            if fried: break
            for j, g in enumerate(gs):
                if i == j: continue
                # If a chip is in the same area as another RTG,
                # and it's not connected to its own RTG.
                if m == g and gs[i] != m:
                    fried = True
                    break
        if fried: continue
    
        singlePicks = [i for i, f in enumerate(ms + gs) if f == curFloor]
        doublePicks = list(set(tuple(sorted((i, j))) for i in singlePicks for j in singlePicks if i != j))
        singlePicks = [(i,) for i in singlePicks]

        n = len(items)
        for move in [1, -1]:
            picks = doublePicks + singlePicks

            nxtFloor = curFloor + move
            if not 0 <= nxtFloor < floorAmt: continue

            for pick in picks:
                nxtItems = [list(mat) for mat in curItems]
                for i in pick: nxtItems[i%n][i//n] += move
                
                nxtState = (nxtFloor, tuple(sorted(tuple(i) for i in nxtItems)))
                queue.append((nxtState, dist+1))

    return None

##########################################################

rawFloors = AOCUtils.loadInput(11)

floors1 = []
for rawFloor in rawFloors:
    if "nothing relevant" in rawFloor:
        floor = []
    else:
        floor = " ".join(rawFloor[:-1].split()[4:])
        floor = [f.split("and") for f in floor.split(",")]
        floor = [item.strip() for f in floor for item in f if item.strip()]
        floor = [" ".join(f.split()[1:]) for f in floor]

    floors1.append(floor)

print("Part 1: {}".format(assemble(floors1, 4)))

floors2 = [f[:] for f in floors1]
floors2[0] += ["elerium generator",
               "elerium-compatible microchip",
               "dilithium generator",
               "dilithium-compatible microchip"]

print("Part 2: {}".format(assemble(floors2, 4)))

AOCUtils.printTimeTaken()