######################################
# --- Day 6: Chronal Coordinates --- #
######################################

import AOCUtils

def getDist(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])

def getAllDistances(p, coords):
    return [getDist(p, c) for c in coords]

######################################

rawCoords = AOCUtils.loadInput(6)

gridSizeX, gridSizeY = 0, 0
coords = []
for i in rawCoords:
    x, y = [int(c) for c in i.split(", ")]
    coords.append((x, y))

    if x > gridSizeX: gridSizeX = x
    if y > gridSizeY: gridSizeY = y

gridSizeX += 1
gridSizeY += 1

distances = [[getAllDistances((i, j), coords) for j in range(gridSizeY)] for i in range(gridSizeX)]

grid = [[None for _ in range(gridSizeY)] for _ in range(gridSizeX)]
for i in range(gridSizeX):
    for j in range(gridSizeY):
        minDist = min(distances[i][j])
        if distances[i][j].count(minDist) <= 1:
            grid[i][j] = distances[i][j].index(minDist)

areas = [0 for _ in range(len(coords))]
for i in range(gridSizeX):
    for j in range(gridSizeY):
        if grid[i][j]: areas[grid[i][j]] += 1

for i in range(gridSizeX):
    if grid[i][0]: areas[grid[i][0]] = 0
    if grid[i][-1]: areas[grid[i][-1]] = 0

for i in range(gridSizeY):
    if grid[0][i]: areas[grid[0][i]] = 0
    if grid[-1][i]: areas[grid[-1][i]] = 0

print("Part 1: {}".format(max(areas)))

count = 0
for i in range(gridSizeX):
    for j in range(gridSizeY):
        if sum(distances[i][j]) < 10000:
            count += 1

print("Part 2: {}".format(count))

AOCUtils.printTimeTaken()