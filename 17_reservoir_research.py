######################################
# --- Day 17: Reservoir Research --- #
######################################

import AOCUtils
from sys import setrecursionlimit
setrecursionlimit(10000)

class Ground:
    def __init__(self, xdim, ydim):
        self.xdim, self.ydim = xdim, ydim
        self.xsize, self.ysize = xdim[1]-xdim[0]+1, ydim[1]-ydim[0]+1
        self.tiles = [["." for _ in range(self.xsize)] for _ in range(self.ysize)]

    def setClay(self, clay):
        for c in clay:
            c = (c[0]-self.xdim[0], c[1]-self.ydim[0])
            self.tiles[c[1]][c[0]] = "#"

    def get(self, pos): return self.tiles[pos[1]][pos[0]] if self.exists(pos) else None
    def set(self, pos, data): self.tiles[pos[1]][pos[0]] = data

    def exists(self, pos): return 0 <= pos[0] < self.xsize and 0 <= pos[1] < self.ysize
    def isBarrier(self, pos): return (self.get(pos) == "#" or self.get(pos) == "~")

    def simulate(self, waterFountain):
        self._simulate((waterFountain[0]-self.xdim[0], waterFountain[1]))

    def _simulate(self, pos):
        self.set(pos, "|")

        down = (pos[0], pos[1]+1)
        left = (pos[0]-1, pos[1])
        right = (pos[0]+1, pos[1])

        if self.get(down) == ".": # If it can still fall, recursive call for down position
            self._simulate(down)

        leftWall = None
        scout = pos[0]
        while scout > 0 and self.isBarrier((scout, pos[1]+1)):
            scout -= 1
            if self.isBarrier((scout, pos[1])):
                leftWall = scout
                break

        rightWall = None
        scout = pos[0]
        while scout < self.xsize and self.isBarrier((scout, pos[1]+1)):
            scout += 1
            if self.isBarrier((scout, pos[1])):
                rightWall = scout
                break

        # If position is bound by two walls, it can be made into still water
        if leftWall and rightWall:
            for i in range(leftWall+1, rightWall):
                self.set((i, pos[1]), "~")
        else: # Otherwise, recursivelly call for left and right positions
            if self.exists(down) and self.get(down) != "|" and self.get(left) == ".":
                self._simulate(left)

            if self.exists(down) and self.get(down) != "|" and self.get(right) == ".":
                self._simulate(right)

    def countElement(self, element): return sum([y.count(element) for y in self.tiles])

######################################

scan = AOCUtils.loadInput(17)

clay = set()
minX, maxX, minY, maxY = None, None, None, None

for s in scan:
    s = s.split(", ")
    x = s[0].split("=")[1] # Assume first coordinates are x
    y = s[1].split("=")[1]
    if s[0][0] == "y": x, y = y, x # If first coordinares are y, swap

    x0, x1 = ([int(i) for i in x.split("..")]) if ".." in x else (int(x), int(x))
    if not minX or x0 < minX: minX = x0
    if not maxX or x1 > maxX: maxX = x1

    y0, y1 = ([int(i) for i in y.split("..")]) if ".." in y else (int(y), int(y))
    if not minY or y0 < minY: minY = y0
    if not maxY or y1 > maxY: maxY = y1

    for x in range(x0, x1+1):
        for y in range(y0, y1+1):
            clay.add((x, y))

ground = Ground((minX-1, maxX+1), (minY, maxY))
ground.setClay(clay)

ground.simulate((500, 0))

runningWater = ground.countElement("|")
stillWater =  ground.countElement("~")
print("Part 1: {}".format(runningWater + stillWater))
print("Part 2: {}".format(stillWater))

AOCUtils.printTimeTaken()