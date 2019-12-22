#############################
# --- Day 22: Mode Maze --- #
#############################

import AOCUtils
from heapq import heappush, heappop

# Equipment X is not allowed in region X
ROCKY, WET, NARROW = 0, 1, 2
NEITHER, TORCH, CLIMBING = 0, 1, 2

BORDER = 100

class Cave:
    def __init__(self, depth, target, size):
        self.depth = depth
        self.target = target
        self.size = size

        self.geoIndex = [[None for _ in range(self.size[1])] for _ in range(self.size[0])]
        for y in range(self.size[0]):
            for x in range(self.size[1]):
                self.geoIndex[y][x] = self.getGeo((x, y))

    def getErosion(self, pos):
        return (self.geoIndex[pos[1]][pos[0]] + self.depth) % 20183

    def getGeo(self, pos):
        if pos == (0, 0) or pos == (self.target[1], self.target[0]):
            return 0
        elif pos[0] == 0:
            return pos[1] * 16807
        elif pos[1] == 0:
            return pos[0] * 48271
        else:
            return self.getErosion((pos[0]-1, pos[1])) * self.getErosion((pos[0], pos[1]-1))

    def getRiskLevel(self):
        risk = 0
        for y in range(self.target[0]+1):
            for x in range(self.target[1]+1):
                risk += (self.getErosion((x, y)) % 3)
        return risk

    def getFastestPath(self):
        heap = [(0, (0, 0), TORCH)]
        visited = {(0, TORCH): 0}

        def step():
            for delta in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                npos = (pos[0]+delta[0], pos[1]+delta[1])
               
                if (npos, equip) in visited and visited[(npos, equip)] <= time: continue # There is a faster path
                if npos[0] < 0 or npos[0] >= self.size[1] or npos[1] < 0 or npos[1] >= self.size[0]: continue # Out of bounds
                if self.getErosion(npos) % 3 == equip: continue # Equipment not allowed

                visited[(npos, equip)] = time
                heappush(heap, (time, npos, equip))

        while len(heap) > 0:
            time, pos, equip = heappop(heap)
            
            if pos == (self.target[1], self.target[0]) and equip == TORCH: # Reached target
                break

            time += 1 # No change in equipment
            step()

            time += 7 # Change in equipment
            for equip in [(equip+1)%3, (equip+2)%3]:
                if self.getErosion(pos) % 3 != equip: # Only equipments that are allowed in next region
                    step()

        return time

#############################

rawInput = AOCUtils.loadInput(22)
depth = int(rawInput[0].split()[1])
target = tuple([int(i) for i in rawInput[1].split()[1].split(",")])

cave = Cave(depth, target, (target[0]+BORDER, target[1]+BORDER))

print("Part 1: {}".format(cave.getRiskLevel()))

print("Part 2: {}".format(cave.getFastestPath()))

AOCUtils.printTimeTaken()