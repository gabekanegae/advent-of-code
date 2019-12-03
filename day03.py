#############################################
# --- Day 3: No Matter How You Slice It --- #
#############################################

import AOCUtils

#############################################

rawClaims = AOCUtils.loadInput(3)

claims = []
for claim in rawClaims:
    claimID = int(claim[1:].split()[0])
    startX, startY = [int(a) for a in claim.split()[2][:-1].split(",")]
    sizeX, sizeY = [int(a) for a in claim.split()[3].split("x")]

    claims.append((claimID, startX, startY, sizeX, sizeY))

fabric = {}

for claim in claims:
    claimID, startX, startY, sizeX, sizeY = claim

    for dx in range(sizeX):
        for dy in range(sizeY):
            pos = (startX+dx, startY+dy)
            if pos not in fabric:
                fabric[pos] = 1
            else:
                fabric[pos] += 1
                unique = False

overlaps = sum([amt > 1 for amt in fabric.values()])
print("Part 1: {}".format(overlaps))

for claim in claims:
    claimID, startX, startY, sizeX, sizeY = claim

    unique = True
    for dx in range(sizeX):
        if not unique: break
        for dy in range(sizeY):
            pos = (startX+dx, startY+dy)
            if fabric[pos] > 1:
                unique = False
                break

    if unique:
        print("Part 2: {}".format(claimID))
        break

AOCUtils.printTimeTaken()